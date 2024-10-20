class MyPlayer:
    '''Hrac vyhodnoti vstup a vybere vhodnou strategii, prohazuje strategie'''
    def __init__(self, payoff_matrix, number_of_iterations=None):
        #nacteni vstupnich hodnot, nastaveni konstant
        self.COOPERATE = False
        self.DEFECT = True
        self.matrix = payoff_matrix
        self.choose_strat()
        if number_of_iterations != None:
            self.rounds_remaining = number_of_iterations
        else: self.rounds_remaining = -1
        #forgiveness counter
        #snizuje ochotu odpoustet po opakovanych zradach
        self.forgiveness = 0
        self.num_of_defects = 0

    def choose_strat(self):
        #vyhodnoceni vstupni payout matice, vyber strategie
        if sum(self.matrix[0][0]) < sum(self.matrix[1][1]):
            if self.matrix[0][0][0] < self.matrix[1][0][0] and self.matrix[0][1][0] < self.matrix[1][1][0]:
                self.strat = "only_D"
                self.my_last_move = self.DEFECT
            else:
                self.strat = "reverse_strat"
                #nastaveni prommenych na prvni tah
                self.my_last_move = self.COOPERATE
                self.opp_last_move = self.DEFECT
        else:
            if self.matrix[0][0][0] > self.matrix[1][0][0] and self.matrix[0][1][0] > self.matrix[1][1][0]:
                self.strat = "only_C"
                self.my_last_move = self.COOPERATE
            else:
                self.strat = "default_strat"
                #nastaveni promennych na prvni tah
                self.my_last_move = self.COOPERATE
                self.opp_last_move = self.COOPERATE


    def select_move(self):
        match self.strat:
            case "only_C":
                return self.COOPERATE

            case "only_D":
                return self.DEFECT

            case "default_strat":
                if self.rounds_remaining == 1:
                    return self.DEFECT
                else:
                    if self.opp_last_move == self.DEFECT:
                        #hrac zkousi kooperovat po exponencialnim poctu zrad (1,2,4,8,16 atd...)
                        if (2**self.forgiveness <= self.num_of_defects) and (self.my_last_move == DEFECT):
                            self.forgiveness += 1
                            self.num_of_defects = -2
                            return self.COOPERATE
                        elif self.num_of_defects < 0:
                            return self.COOPERATE
                        else: 
                            return self.DEFECT
                        self.num_of_defects +=1
                    else:
                        return self.my_last_move

            case "reverse_strat":
                if self.rounds_remaining == 1:
                    return self.COOPERATE
                else:
                    if self.opp_last_move == self.COOPERATE:
                        #hrac zkousi kooperovat po exponencialnim poctu zrad (1,2,4,8,16 atd...)
                        #v tomto pripade defect neznamenÃ¡ primo krok defect, ale greedy krok cooperate
                        if (2**self.forgiveness <= self.num_of_defects) and (self.my_last_move == COOPERATE):
                            self.forgiveness += 1
                            self.num_of_defects = -2
                            return self.DEFECT
                        elif self.num_of_defects < 0:
                            return self.DEFECT
                        else: 
                            return self.COOPERATE
                        self.num_of_defects +=1
                    else:
                        return self.my_last_move


    def record_last_moves(self, my_last_move, opponent_last_move):
        #hrac zapocita tah
        self.rounds_remaining -= 1
        #zkontroluje potencionalni sum, pripadne opravi svuj zaznam
        if self.my_last_move == my_last_move:
            self.my_last_move = my_last_move
        else: self.my_last_move = not my_last_move
        #hrac neresi souperuv sum. To je souperuv problem :)
        self.opp_last_move = opponent_last_move