Design multiplayer ludo game

- User play ludo with friends/strangers
- we roll dice(1,6) with random number appearing in.
- the first one to reach 100 will win.
- if we encounter snakes we drop off to tip of snake
- if we encounter ladder we climb up the top of ladder.

Db schema design

1. Player
    - id
    - name
    - email
    - username
    - created_at
    - last_login_at
    - is_active
   
2. Dice
   - game id
   - number
   - user id(who rolled the dice)
   - datetime
   

3. Snake/Ladder
   - id
   - game id
   - start
   - end
   

4. Game Move History
   - id
   - user id(who rolled the dice)
   - game id
   - dice number
   - curr_position
   - new position
   - datetime


5. Leaderboard
   - id
   - game id
   - player id
   - position
   - updated_at


6. Game
    - id
    - start time
    - end time
    - winner(fk to player id)
    - player count
    - snake count
    - ladder count
    - duration
    - game_status
   
   
7. Player-Game
   - id
   - player id
   - game id