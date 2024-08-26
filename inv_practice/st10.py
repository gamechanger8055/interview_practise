'''
/***
 * Background
 * Our users have points in their accounts.
 * Users only see a single balance in their accounts.
 * But for reporting purposes we actually track their points per payer/partner.
 * In our system, each transaction record contains:
 *    payer (String), points (String), timestamp (date).
 * For earning points it is easy to assign a payer, we know which actions earned the points.
 * And thus which partner should be paying for the points.
 *
 * When a user spends points, they don't know or care which payer the points come from.
 * But, our accounting team does car how the points are spent.
 * There are two rules for determining what points to "spend" first:
 *    We want the oldest points to be spent first
 *    We want no payer's points to go negative
 *
 * You need to do:
 *    Add transaction for a specific payer and date.
 *    Spend points using the rules above and return a list of
 *       {"payer": <string>, "points": <integer>} for each call
 *    Return all payer point balances.
 *
 * Example
 * Suppose you call your add transaction route with the following sequence of calls:
 *    { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
 *    { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }
 *    { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }
 *    { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
 *    { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
 *
 * Then you call your spend points route with the following request:
 *    { "points": 5000 }
 * The expected response from the spend call would be:
 *    [
 *       { "payer": "DANNON", "points": -100 },
 *       { "payer": "UNILEVER", "points": -200 },
 *       { "payer": "MILLER COORS", "points": -4,700 }
 *    ]
 * A subsequent call to the points balance route, after the spend, should returns the following results:
 *    {
 *       "DANNON": 1000,
 *       "UNILEVER": 0,
 *       "MILLER COORS": 5300
 *    }
 *
 * FAQ: For any requirements not specified via an example, use your best judgement to determine the expected result.
 */
'''

from datetime import datetime
from collections import defaultdict, deque

class PointsManager:
    def __init__(self):
        self.transactions=deque()
        self.balances=defaultdict(int)

    def add_transaction(self,payer,points,timestamp):
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        self.transactions.append((timestamp, payer, points))
        self.balances[payer] += points

    def spend_points(self, points):
        self.transactions = deque(sorted(self.transactions, key=lambda x: x[0]))  # Sort by timestamp
        spend_details = []
        points_to_spend = points

        temp_balances = self.balances.copy()  # To check for negative balances

        while points_to_spend > 0 and self.transactions:
            timestamp, payer, available_points = self.transactions.popleft()
            points_to_use = min(available_points, points_to_spend)

            if available_points > 0:
                temp_balances[payer] -= points_to_use
                if temp_balances[payer] >= 0:
                    points_to_spend -= points_to_use
                    spend_details.append({"payer": payer, "points": -points_to_use})
                    self.balances[payer] -= points_to_use
                    if available_points - points_to_use != 0:
                        self.transactions.appendleft((timestamp, payer, available_points - points_to_use))
                else:
                    temp_balances[payer] += points_to_use
                    self.transactions.appendleft((timestamp, payer, available_points))
            else:
                self.transactions.appendleft((timestamp, payer, available_points))

        return spend_details

    def get_balances(self):
        return dict(self.balances)


pm = PointsManager()
pm.add_transaction("DANNON", 1000, "2020-11-02T14:00:00Z")
pm.add_transaction("UNILEVER", 200, "2020-10-31T11:00:00Z")
pm.add_transaction("DANNON", -200, "2020-10-31T15:00:00Z")
pm.add_transaction("MILLER COORS", 10000, "2020-11-01T14:00:00Z")
pm.add_transaction("DANNON", 300, "2020-10-31T10:00:00Z")

print(pm.spend_points(5000))
# Expected: [{'payer': 'DANNON', 'points': -100}, {'payer': 'UNILEVER', 'points': -200}, {'payer': 'MILLER COORS', 'points': -4700}]

print(pm.get_balances())
# Expected: {'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300}