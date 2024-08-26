import threading
import time


class MovieTicketingSystem:
    def __init__(self,movies:dict):
        self.movies=movies
        self.lock=threading.Lock()

    def get_search(self):
        results=[]
        for movie_id,movie_info in self.movies.items():
            for showtime_id,showtime_info in movie_info['showtimes'].items():
                if showtime_info['available_tickets']>0:
                    results.append({
                        "movie_id": movie_id,
                        "name": movie_info['name'],
                        "showtime_id": showtime_id,
                        "time": showtime_info['time'],
                        "available_tickets": showtime_info['available_tickets']
                    })
        return results

    def post_book_ticket(self,movie_id,showtime_id):
        with self.lock:
            if movie_id not in movies or showtime_id not in movies[movie_id]['showtimes']:
                return {"error": "Movie or showtime not found"}

            showtime_info = movies[movie_id]['showtimes'][showtime_id]

            if showtime_info['available_tickets']<= 0:
                return {"error": "No tickets available"}

            showtime_info['available_tickets']-=1

            return {"success": "Ticket booked successfully", "remaining_tickets": showtime_info['available_tickets']}




movies = {
    "movie_id_1": {
        "name": "Movie 1",
        "showtimes": {
            "showtime_1": {
                "time": "2024-07-27T15:00:00",
                "available_tickets": 100
            }
        }
    }
}

movieTicket=MovieTicketingSystem(movies)
curr_time=time.time()
for i in range(50):
    movieTicket.post_book_ticket("movie_id_1","showtime_1")
sync=time.time()-curr_time

# movieTicket.post_book_ticket("movie_id_1","showtime_1")
curr_time=time.time()

threads=[]
for i in range(50):
    thread=threading.Thread(target=movieTicket.post_book_ticket,args=("movie_id_1","showtime_1"))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
asynct=time.time()-curr_time
print(asynct-sync)


print(movieTicket.get_search())
