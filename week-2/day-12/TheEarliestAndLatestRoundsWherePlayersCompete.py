class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        def simulate_fixed_strategy(strategy_func):
            players = list(range(1, n + 1))
            round_num = 1
            
            while True:
                if len(players) <= 2:
                    break

                idx1 = players.index(firstPlayer)
                idx2 = players.index(secondPlayer)
                if idx1 + idx2 == len(players) - 1:
                    break 

                num_current_players = len(players)
                next_round_players = set()
                
                for i in range(num_current_players // 2):
                    p1 = players[i]
                    p2 = players[num_current_players - 1 - i]

                    if p1 == firstPlayer or p2 == firstPlayer:
                        next_round_players.add(firstPlayer)
                    elif p1 == secondPlayer or p2 == secondPlayer:
                        next_round_players.add(secondPlayer)
                    else:
                        winner = strategy_func(p1, p2)
                        next_round_players.add(winner)
                
                if num_current_players % 2 == 1:
                    next_round_players.add(players[num_current_players // 2])
                
                players = sorted(list(next_round_players))
                round_num += 1
            
            return round_num

        latest_min_wins = simulate_fixed_strategy(min) 
        latest_max_wins = simulate_fixed_strategy(max) 
        latest = max(latest_min_wins, latest_max_wins)
        initial_state = tuple(range(1, n + 1))
        queue = deque([(initial_state, 1)])
        visited = {initial_state}

        while queue:
            current_players_tuple, round_num = queue.popleft()
            idx1 = current_players_tuple.index(firstPlayer)
            idx2 = current_players_tuple.index(secondPlayer)
            if idx1 + idx2 == len(current_players_tuple) - 1:
                earliest = round_num
                return [earliest, latest]

            num_players = len(current_players_tuple)
            choice_matches = []
            base_winners = set()
            
            for i in range(num_players // 2):
                p1, p2 = current_players_tuple[i], current_players_tuple[num_players - 1 - i]
                if p1 == firstPlayer or p2 == firstPlayer:
                    base_winners.add(firstPlayer)
                elif p1 == secondPlayer or p2 == secondPlayer:
                    base_winners.add(secondPlayer)
                else:
                    choice_matches.append((p1, p2))
            
            if num_players % 2 == 1:
                base_winners.add(current_players_tuple[num_players // 2])
            
            def generate_outcomes(match_idx, current_winners):
                if match_idx == len(choice_matches):
                    next_state = tuple(sorted(list(current_winners)))
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, round_num + 1))
                    return

                p1, p2 = choice_matches[match_idx]
                current_winners.add(p1)
                generate_outcomes(match_idx + 1, current_winners)
                current_winners.remove(p1) 
                current_winners.add(p2)
                generate_outcomes(match_idx + 1, current_winners)
                current_winners.remove(p2) 

            generate_outcomes(0, base_winners)

        return [-1, -1] 
