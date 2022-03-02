import string
pessoa = "";
salario = float(0);
lista_salario_pessoa = [];
val = [];


while pessoa != "sair":
    print("Digite o nome da pessoa: ");
    pessoa = input();
    print("Digite o salário da pessoa: ");
    salario = input();
    item_salario_pessoa = [pessoa, salario];
    lista_salario_pessoa.append(item_salario_pessoa);
    print("Deseja add + pessoa | Digite 'continuar' ou 'sair'");
    pessoa = input();



for i in range(200,4000):
    abc = str(i);
    count = 0;
    func_nome_cat = [];
    if((abc.find("00")!=-1) or (abc.find("000")!=-1)):
        for element in lista_salario_pessoa:
            if((float(element[1]) >= i) and (float(element[1]) <= (i+99)) ) :
                func_nome_cat.append(element[0]);
                count += 1
        val.append({'Indice: ':len(val),'Salário renge inicial: ':i,'Salário range final: ':i+99,'Quantidade de pessoas: ': count,'Nome: ': func_nome_cat});
    

for item_val in val:
    print(item_val);


print("Digite um salário para buscar a posição na lista: ");
buscar_salario = input();

def build_dict(seq, key):
    return dict((d[key], dict(d, indice=index)) for (index, d) in enumerate(seq))

busca = build_dict(val, key="Salário renge inicial: ")
resultado = busca.get(float(buscar_salario))

print(resultado);
