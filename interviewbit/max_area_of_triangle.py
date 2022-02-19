from math import ceil


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0])
        
        inverse_pair = {
            'r': 'gb',
            'g': 'rb',
            'b': 'rg'
        }

        right_most_x = { 'r': -1, 'g': -1, 'b': -1 }
        left_most_x = { 'r': m, 'g': m, 'b': m }
        down_most_y, possible_bases = [], []

        for i in range(0, m):
            current_down_most_y = { 'r': -1, 'g': -1, 'b': -1 }
            for j in range(0, n):
                ch = A[j][i]
                
                current_down_most_y[ch] = max(current_down_most_y[ch], j)
                
                right_most_x[ch] = max(right_most_x[ch], i)
                left_most_x[ch] = min(left_most_x[ch], i)

            down_most_y.append(current_down_most_y)

        for i in range(0, m):
            cur_max_gb, cur_max_rb, cur_max_rg = 0, 0, 0
            for j in range(0, n):
                ch = A[j][i]
                if ch == 'r':
                    cur_max_rb = max(cur_max_rb, down_most_y[i]['b'] - j + 1)
                    cur_max_rg = max(cur_max_rg, down_most_y[i]['g'] - j + 1)
                elif ch == 'g':
                    cur_max_gb = max(cur_max_gb, down_most_y[i]['b'] - j + 1)
                    cur_max_rg = max(cur_max_rg, down_most_y[i]['r'] - j + 1)
                else:
                    cur_max_gb = max(cur_max_gb, down_most_y[i]['g'] - j + 1)
                    cur_max_rb = max(cur_max_rb, down_most_y[i]['r'] - j + 1)

            possible_bases.append({
                'gb': cur_max_gb,
                'rb': cur_max_rb,
                'rg': cur_max_rg
            })

        max_area = 0

        for ch in ['r', 'g', 'b']:
            for i in range(0, m):
                possible_base = possible_bases[i][inverse_pair[ch]]
                possible_height_1 = right_most_x[ch] - i + 1
                possible_height_2 = i - left_most_x[ch] + 1

                max_area = max(max_area, int(ceil(0.5 * possible_base * possible_height_1)))
                max_area = max(max_area, int(ceil(0.5 * possible_base * possible_height_2)))

        return max_area
