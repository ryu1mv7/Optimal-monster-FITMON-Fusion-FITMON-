def fuse(fitmons):
    """
    Function description:
        This function return possible highest cuteness score after fusing given a list of fitmons as input.
        Each fitmon is represented as [affinity_left,cuteness_score, affinity_right], and cuteness_score after fusing is calculated according to formula.
        Fusing only happens b/w adjacent two monsters.
    Approach description:
        To avoid recomputation of each phase of fusing, I prepare 2D memo that store a optimal fitmon which has optimal(highest) cuteness score in the specific range of "left" to "right"(inclusive) in given input fitmons.
        The variables, left and right point the fitmon at the the left or right edge that will be used for fusing.
        For example, given, [[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]] as a input, if left pont to [0, 29, 0.9], right point to [0.8, 48, 0], 
        memo[left][right] returns the fitmon that has a highest possible cuteness score as a result of fusing from fitmons,  [0, 29, 0.9] all the way to [0.8, 48, 0], which is highest cuteness score among all monsters.
        Firstly, I create n * n 2D list and initialise each entry(cell) of this memo by [0,0,0], not only cuteness score but also affinity_left and affinity_right because they are necessary for formula in each fusing phase.
        Then, I assign a input of fitmons to the memo diagonally in where memo[i-1][i-1] sequentially first fitmon(i = 1), 2nd fitmon(i = 2) and so on... and this will be the base case. When there is only one fitmon(No fuse), optimal fitmon is the fitmon itself.
        From this base case, I start calculating(finding) optimal fitmon by increasing the range(length) of the number of fitmons to fuse. Finally, if I get the optimal fitmon from all of fitmons in the input, which means that is the answer.
        The most outer loop specify the length or the number of fitmons I take for fusing, and in the middle loop I decide the value of left and right according to the number of fitmons I can think or use for fusing.
        Then, in the most inner loop, I divide sub array(left to right) into additionally left to k, k+1 to right and checks and get which fusing would get the highest possible cuteness score.
    Input:
        fitmons: a list of fitmon, each fitmon is represented as [affinity_left,cuteness_score, affinity_right]. affinity_left and affinity_right are the float, and cuteness_score is the integer.
    Return:
        cuteness_score: integer, possible highest cuteness score after fusing given a list of fitmons as input.

    Time complexity: O(N^3) where N is the number of items(fitmons) in the list, fitmons.
        Time complexity analysis: The block of the most inner loop takes O(1) operations such as index access and math calculation. 
        Then, there are 3 loops that iterate (N - x) times each (x is the constant number), so overall takes O(N^3). Other operations such as creating memo and initilizing base cases takes less than O(N^3) (O(N^2), O(N) accordingly)
    Space complexity: O(N^2) where N is the number of items(fitmons) in the list, fitmons. Since input takes O(N) and Aux takes O(N^2), overall is O(N^2)
        Input space analysis: input is 1D list(N sized) and each cell has fixed number of components(3)-> O(3N) = O(N)
        Aux space analysis:: I created 2D list(N* N sized) and each cell has fixed number of components(3). Therefore, Aux space is O(N^2)
    """
    n = len(fitmons)
    
    # create 2D list/ each cell represent optimal [affinity_left,cuteness_score, affinity_right] 
    # memo[i][j] shows optimal fitmon after fusing of fitmons from i th fitmon to j th fitmon in a input (i <= j)
    memo = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    
    # Assign base case first: only one fitmon(no fusing)
    for i in range(n):
        memo[i][i][0] = fitmons[i][0]
        memo[i][i][1] = fitmons[i][1]
        memo[i][i][2] = fitmons[i][2]


    for length in range(2, n + 1): # decide the number of fitmons I use for fusing
        for left in range(0, n - length + 1): # from that number of fitmons I can use for fusing, think all combinations of left and right 
            right = left + length - 1
            for k in range(left, right): # calc all possible fusing in specific phase(given particular length, left and right), and choose the optimal fitmon that has highest cuteness score.
                affinity_left = memo[left][k][0]
                affinity_right = memo[k+1][right][2]
                cuteness_score = memo[left][k][1] * memo[left][k][2] + memo[k+1][right][1] * memo[k+1][right][0]
                cuteness_score = int(cuteness_score)
                if memo[left][right][1] < cuteness_score:
                    memo[left][right] = [affinity_left,cuteness_score,affinity_right]
    return memo[0][n-1][1] # return the cuteness score of all monsters given as a input

if __name__ == "__main__":
    a = fuse([[0, 30, 0.6],
[0.6, 20, 0.2],
[0.2, 90, 0.9],
[0.9, 50, 0]])
    print(a) # expect 72
