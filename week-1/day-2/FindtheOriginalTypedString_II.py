MOD = 10**9 + 7
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        runs = [1]
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                runs[-1] += 1
            else:
                runs.append(1)

        total_combinations = 1
        for freq in runs:
            total_combinations = (total_combinations * freq) % MOD

        if len(runs) >= k:
            return total_combinations

        count = [0] * k
        new_count = [0] * k
        prefix_sum = [0] * k
        count[0] = 1  

        for freq in runs:
            prefix_sum[0] = count[0]
            for i in range(1, k):
                prefix_sum[i] = (prefix_sum[i - 1] + count[i]) % MOD

            for i in range(1, k):
                right = prefix_sum[i - 1]
                left = prefix_sum[i - 1 - freq] if i - 1 - freq >= 0 else 0
                new_count[i] = (right - left + MOD) % MOD

            count, new_count = new_count, [0] * k

        invalid_combinations = sum(count) % MOD
        return (total_combinations - invalid_combinations + MOD) % MOD
