from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        # only winners will have not lost any matches, therefore = 0
        # only losers will potentially have lost one match, therefore = 1
        # those neither 1 or 0 will be -1, not in contention
        none_or_one = {}

        for match in matches:
            winner = match[0]
            loser = match[1]

            if winner not in none_or_one:
                none_or_one[winner] = 0
            
            if loser not in none_or_one:
                none_or_one[loser] = 1
            else:
                if none_or_one[loser] >= 1:
                    none_or_one[loser] = -1
                else:
                    none_or_one[loser] += none_or_one.get(loser, 0) + 1

        print(none_or_one)

        winners = []
        losers = []
        for k in none_or_one:
            if none_or_one[k] == 0:
                winners.append(k)
            if none_or_one[k] == 1:
                losers.append(k)
        
        return [sorted(winners), sorted(losers)]
        '''

        # another solution, reduce complexity of using key/value pairs
        winners = set()
        losers = set()
        out_of_contention = set()

        for match in matches:
            winner = match[0]
            loser = match[1]

            if winner not in losers and winner not in out_of_contention:
                winners.add(winner)

            if loser in winners:
                winners.remove(loser)
                losers.add(loser)
            elif loser in losers:
                losers.remove(loser)
                out_of_contention.add(loser)
            elif loser not in out_of_contention:
                losers.add(loser)
            

        return [sorted(list(winners)), sorted(list(losers))]




sol = Solution()
print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(sol.findWinners([[2,3],[1,3],[5,4],[6,4]]))
print(sol.findWinners([[132,71],[71,132]]))
print(sol.findWinners([[132,71],[71,132]]))
print(sol.findWinners([[10245,43823],[13632,50046],[20362,62395],[38675,96507],[42444,90905],[62017,25001],[67125,60162],[89282,95903],[95143,10211],[98000,816]]))
print(sol.findWinners([[2,4],[2,8],[5,10],[6,5],[7,2],[7,6],[7,9],[8,3],[8,7],[9,1]]))
print(sol.findWinners([[1,2],[1,4],[1,5],[2,1],[3,1],[3,2],[4,3],[4,5],[5,3],[5,4]]))
print(sol.findWinners([[1586,60784],[2170,46474],[2714,84577],[3461,60160],[4004,3641],[6003,41317],[6183,98619],[6195,21555],[6940,9104],[8035,81079],[8371,55164],[9654,14896],[10326,18163],[10527,32130],[11109,54407],[11604,8670],[13339,36260],[14952,62478],[15597,16615],[16982,68880],[17822,46327],[18002,32941],[20186,86017],[21760,29167],[23656,9127],[23698,59546],[23743,39176],[24235,3316],[26805,94843],[26829,44671],[28309,6749],[29666,5626],[29845,61606],[30902,85559],[31086,8113],[31285,90485],[32623,32530],[33992,36463],[34749,24514],[36032,64526],[37976,73150],[38223,1463],[39951,61405],[40672,53433],[40993,13521],[41918,98997],[42341,66059],[44428,78326],[46164,79512],[49294,16565],[49777,65595],[50547,91591],[52981,60290],[53273,3338],[53331,9371],[54531,79758],[55772,72438],[58770,9020],[59188,8198],[59574,76153],[59720,64779],[60020,6427],[60449,85259],[61327,61414],[61443,66521],[61793,93715],[61804,47493],[62691,86680],[63527,41936],[65415,63943],[66454,22228],[66521,19104],[68356,54512],[68490,34099],[68798,85882],[69055,55387],[71832,16667],[73552,19945],[73898,30284],[74228,91715],[74473,27916],[74729,75217],[76234,27673],[78147,37006],[80376,16080],[80888,79105],[82559,51135],[82988,57513],[84637,31355],[85582,4870],[86892,48037],[86904,99538],[87329,1158],[87354,53433],[89199,25927],[89369,57689],[92524,32197],[93741,28923],[95651,57737],[96558,4321]]))
print(sol.findWinners([[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]]))