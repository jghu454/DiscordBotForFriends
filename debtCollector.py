class debt:


  def __init__(self,message):
    self["debtTable"] = {
      "OwnerID": message.author.id,
      "MoneyOwed": {


      }
      
    }
  
  def addMoney(self, id, money, message):
    person = self["debtTable"]["MoneyOwed"][id]
    
    if person is None:
      self["debtTable"]["MoneyOwed"][id] = float(money)
      message.channel.send("Creating Debt")
    elif person:
      self["debtTable"]["MoneyOwed"][id] += float(money)
      message.channel.send("Adding Debt")

  def removeMoney(self, id, money, message):
    person = self["debtTable"]["MoneyOwed"][id]
    if person is None:
      message.channel.send("Person has no debt")
    elif person:
      self["debtTable"]["MoneyOwed"][id] += float(money)
      message.channel.send("Subtracting Debt")

      




