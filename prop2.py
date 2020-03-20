class gamingCompany(object):
    def reward(self):
      raise NotImplementedError("reward() method is not implemented.")


class money(gamingCompany):
    def reward(self):
       print("money reward")

class ammo(gamingCompany):
    def reward(self):
       print ("ammo reward")
class guns(gamingCompany):
    def reward(self):
       print("guns reward")
class score(gamingCompany):
    def reward(self):
       print("score reward")

class RewardFactory(object):

    def getReward(self, rewardName):
      if rewardName == "ammo":
           return ammo()
      elif rewardName == "money":
            return money()
      elif rewardName == "guns":
            return guns()
      elif rewardName == "score":
            return score()
      else:
           return None

stringsArr = ["money","ammo","money","ammo","guns"]

def main():
  factory = RewardFactory()
  for x in stringsArr:
      reward1 = factory.getReward(x)
      reward1.reward()

main()

stringsArr = ["money","ammo","score", "money","ammo","guns"]
main()