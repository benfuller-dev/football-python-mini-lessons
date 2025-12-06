def xg_battle(team_xg, opp_xg, tolerance=0.25):
        """
        return 1 If team_xg is greater than opp_xg + tolerance
        return 0 if team_xg-opp_xg is less than or equal to tolerance
        return -1 if team_xg is less than opp_xg and outside of tolerance
        """

        if team_xg > opp_xg + tolerance:
                return 1
        elif abs (team_xg-opp_xg)<=tolerance:
                return 0
        else:
                return -1
               
print(xg_battle(0.67, 1.6))
print(xg_battle(1.8, 0.4))
print(xg_battle(0.96, 1.1))
