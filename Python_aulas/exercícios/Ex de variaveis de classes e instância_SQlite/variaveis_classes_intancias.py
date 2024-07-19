class Profissional:
    empresa = "Empresa Google"


#self é uma variável de instância
    def __init__(self, nome, profissão):
        self.nome = nome
        self.profissão = profissão

    def __str__(self) -> str:
        return f"{self.nome} - {self.profissão} - {self.empresa}"
    
trab_1 = Profissional("João", "gerente")
trab_2 = Profissional("Pedro", "analista")

print(trab_1)
print(trab_2)
