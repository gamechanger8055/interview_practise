from dataclasses import dataclass, field
from typing import Optional, Callable, TypeVar, Union, Tuple

T = TypeVar('T')

@dataclass(frozen=True)
class DatabaseResult:
    data: Optional[T]
    succeeded: bool = True

    def __bool__(self) -> bool:
        return self.succeeded

DatabaseResult.FAIL = DatabaseResult(None, False)

@dataclass(frozen=True)
class CircuitBreakerResult:
    db_result: Optional[DatabaseResult]
    accepted: bool = True

    def __bool__(self) -> bool:
        return self.accepted and self.db_result.succeeded if self.db_result else False

CircuitBreakerResult.REJECT = CircuitBreakerResult(None, False)
CircuitBreakerResult.FAIL = CircuitBreakerResult(DatabaseResult.FAIL, True)

@dataclass(frozen=True)
class Closed:
    failedCount: int

    def on_success(self) -> 'Closed':
        return CLOSES[0]

    def on_error(self) -> 'Union[Closed, Open]':
        return CLOSES[self.failedCount + 1] if self.failedCount < 1 else OPENS[0]

@dataclass(frozen=True)
class Open:
    rejectedCount: int

    def on_reject(self) -> 'Union[Closed, Open]':
        return OPENS[self.rejectedCount + 1] if self.rejectedCount < 1 else CLOSES[0]

# Cache state instances
OPENS: Tuple[Open, ...] = tuple(Open(i) for i in range(2))
CLOSES: Tuple[Closed, ...] = tuple(Closed(i) for i in range(2))

CircuitBreakerState = Union[Closed, Open]

@dataclass
class CircuitBreaker:
    state: CircuitBreakerState = field(default_factory=lambda: CLOSES[0])

    def call(self, db_call: Callable[[], DatabaseResult[T]]) -> CircuitBreakerResult:
        if isinstance(self.state, Open):
            self.state = self.state.on_reject()
            return CircuitBreakerResult.REJECT
        db_result = db_call()
        self.state = self.state.on_success() if db_result else self.state.on_error()
        return CircuitBreakerResult(db_result)

@dataclass
class DoubleBreaker:
    primary: CircuitBreaker = field(default_factory=CircuitBreaker)
    secondary: CircuitBreaker = field(default_factory=CircuitBreaker)

    def call(self, db_call: Callable[[bool], DatabaseResult[T]]) -> CircuitBreakerResult:
        return self.primary.call(lambda: db_call(True)) or self.secondary.call(lambda: db_call(False))

# Example Usage
if __name__ == "__main__":
    # Mock database call functions
    def successful_db_call(primary: bool) -> DatabaseResult[str]:
        return DatabaseResult(data="Success", succeeded=True)

    def failing_db_call(primary: bool) -> DatabaseResult[str]:
        return DatabaseResult(data=None, succeeded=False)

    # Initialize the DoubleBreaker
    double_breaker = DoubleBreaker()

    # Call the DoubleBreaker with a successful call
    result = double_breaker.call(successful_db_call)
    print(f"Successful call result: {result.db_result.data}, accepted: {result.accepted}")

    # Call the DoubleBreaker with a failing call
    result = double_breaker.call(failing_db_call)
    print(f"Failing call result: {result.db_result.data if result.db_result else 'None'}, accepted: {result.accepted}")
