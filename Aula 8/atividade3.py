import requests

ENDPOINT = "https://viacep.com.br/ws/"
FORMATO_RETORNO_API = "/json/"

def main() -> None:
  cep = input("Digite o número do cep: ")
  cep_valido= validaCEP(cep)
  link = f"{ENDPOINT}{cep_valido}{FORMATO_RETORNO_API}"
  requisicao = requests.get(link)
  resposta = requisicao.json()
  if valida_resposta_requisacao(requisicao):
    uf=resposta.get('uf')
    if uf is None:
       print("Não existe CEP com este endereço!")
    else:
       if verifica_estado_Norte_Nordeste(uf):
          print("Parabéns, você ganhou frete grátis!")
       else:
          print(f"O valor do frete para {cep_valido} é R$19,90")

def validaCEP (cep:str)-> int:
  while len(cep) !=8 or not cep.isdigit():
    if(len(cep) !=8):
      print(f"Você preencheu {len(cep)} digitos no número do CEP. Só é aceito o número de 8 casas!")
    elif not cep.isdigit():
      print(f"Você digitou letra dentro do digitos! Só é permitido número!")   
    cep = input("Digite o número do cep: ")
  return cep

def valida_resposta_requisacao(requisicao: requests.Response)->bool:
  if(requisicao.status_code == 200):
    print("Consulta realizada com SUCESSO!")
    return True
  else:
    print("Erro no servidor! Verifique se o endereço realmente existe no sistema!")
    return False

def verifica_estado_Norte_Nordeste(uf:str)->bool:
  UF_NORTE = ("AC", "AP", "AM", "PA", "RO", "RR", "TO") 
  UF_NORDESTE = ("AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE")
  if uf.upper() in UF_NORTE or uf.upper() in UF_NORDESTE:
        return True
  else:
        return False

##EXECUTA O PROGRAMA
main()










