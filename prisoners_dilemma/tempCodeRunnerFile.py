elif (len(self.other_moves) > 5 and sum(self.other_moves) / len(self.other_moves) > 0.3) and random.random() < 0.05:
            return MyPlayer.DEFECT