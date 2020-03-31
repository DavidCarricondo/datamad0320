
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength    
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        #self.name = name
        super().__init__(health, strength)
        self.name = name #CORRECCIÓN: Primero los atributos heredados, luego los propios, por si hay que sobreescribir alguno

    def receiveDamage(self, damage):
        #self.health -= damage
        super().receiveDamage(damage) #CORRECCIÓN: Aunque cambiemos una función heredada, aún se puede usar la función padre
        if self.health < 1:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"        
    
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    #def __init__(self, health, strength):
    #    super().__init__(health, strength) #CORRECCIÓN: No hay que iniciar saxon porque es igual que la clase padre 
    
    def receiveDamage(self, damage):
    #    self.health -= damage
        super().receiveDamage(damage) #CORRECCIÓN: Igual que en la clase vikings
        if self.health < 1:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"        
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking_damage = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking_damage.attack())
        if saxon.health < 1:
            self.saxonArmy = [e for e in self.saxonArmy if e.health > 0]
        return result

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon_damage = random.choice(self.saxonArmy)
        result = viking.receiveDamage(saxon_damage.attack())
        if viking.health < 1:
            self.vikingArmy = [e for e in self.vikingArmy if e.health > 0]
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


    



