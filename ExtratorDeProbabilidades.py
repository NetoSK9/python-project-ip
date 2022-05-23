import csv
from linecache import cache
from msilib.schema import Error
from operator import contains

class ExtratorDeProbabilidades:
    
    def __init__(self,path, data):
        self.path_csv=path
        self.data_csv=data
    
    #retorna os indices das colunas pretendidas
    def get_index_columns_by_name(self,list_name_columns):
        file=open(self.path_csv,'r')
        
        line_columns = next(iter(file)).split(',')
        list_indice_columns=[]
        
        for column_pretend in list_name_columns:
            for column in line_columns:
                if (column_pretend==column):
                    list_indice_columns.append(line_columns.index(column))
        
        file.close()
        return ( list_indice_columns )
    
    #retorna o indice de uma coluna    
    def get_index_column_by_name(self,name):
        response =-1
        for i in range(len(self.data_csv)):
            list_column_pretend=self.data_csv[i]
            for column_pretend in list_column_pretend:
                if(name==column_pretend):
                    response =  list_column_pretend.index(name)
                    return(response)
        return(response)
    
    #retorna uma lsita com todos os dados em uma dada coluna
    def select_column_by_name(self, name_colum):
        index_colum= self.get_index_column_by_name(name_colum)
        if(index_colum!=-1):
            list_data=[]
            for data in self.data_csv:
                list_data.append(data[index_colum])
            print(list_data)
            return list_data
        else:
            print_error("Coluna nao encontrada")
            return []
    
    def filter_data_column_by_value(self,column,value):
        list_data=[]
        for val in column:
            if (val==value):
                list_data.append()
    
    def list_data(self, num):
        file = open(self.path_csv,'r')
        response=[]
        for i in range(num):
            response.append( next(iter(file)).split(',') )

        file.close()
        return response
    
    def carregar_colunas(self,lista_colunas, quantidade):
        
        
        try:
            file = open(self.path_csv,'r')
            
            list_index_columns = self.get_index_columns_by_name(lista_colunas)
            
            for i in range(quantidade):
                list_line = next(iter(file)).split(',')
                list_auxi=[]
                for index in list_index_columns:
                    list_auxi.append(list_line[index])
                self.data_csv.append(list_auxi)

            file.close()
        except:
            print_error("caminho especificado esta errado!")
        
    def descarregar(self):
        self.data_csv=[] 
        
    def probabilidade_apriori(self,caracteristica, valor):
        print(caracteristica)
        cont_caracteristica_pretend=0.0
        
        caracteristicas_totais=float(len(self.select_column_by_name(caracteristica))-1)
        
        for value in self.select_column_by_name(caracteristica):
            print("Value: "+value)
            print("Valor: "+valor)
            if(value==valor):
                print("entrou no if")
                cont_caracteristica_pretend+=1
        
        response= cont_caracteristica_pretend/caracteristicas_totais
        
        return response
    
    def probabilidade_intervalo(self,caracteristica, inicio,fim):
           
        cont_caracteristica_pretend=0.0
        
        caracteristicas_totais=float(len(self.select_column_by_name(caracteristica))-1)
        
        print(self.select_column_by_name(caracteristica))
        for value in self.select_column_by_name(caracteristica):
            if(value!=caracteristica):
                try:
                    if(inicio<int(value)<fim):
                        cont_caracteristica_pretend+=1
                except:
                    next
        
        response= cont_caracteristica_pretend/caracteristicas_totais
        
        return response
        
    def probabilidade_condicional(self,caracteristica_1, valor_1, caracteristica_2, valor_2):
        cont_caracteristica_pretend=0.0
        
        list_caracteristicas_1=self.select_column_by_name(caracteristica_1)
        list_caracteristicas_2=self.select_column_by_name(caracteristica_2)
        caracteristicas_totais=float(len(self.data_csv)-1)
        
        for i in range(len(self.data_csv)):
            
            if((list_caracteristicas_1[i]==valor_1) and (list_caracteristicas_2[i]==valor_2)):
                cont_caracteristica_pretend+=1
        
        response= cont_caracteristica_pretend/caracteristicas_totais
        
        return response

    def probabilidade_apriori_intervalo(self,caracteristica_1, valor_1, caracteristica_2, inicio,fim):
           
        cont_caracteristica_pretend=0.0
        
        list_caracteristicas_1=self.select_column_by_name(caracteristica_1)
        list_caracteristicas_2=self.select_column_by_name(caracteristica_2)
        caracteristicas_totais=float(len(self.data_csv)-1)
        
        for i in range(len(self.data_csv)):
            if(list_caracteristicas_2[i]!=caracteristica_2):
                if((list_caracteristicas_1[i]==valor_1) and (inicio < int(list_caracteristicas_2[i]) < fim ) ):
                    cont_caracteristica_pretend+=1
        
        response= cont_caracteristica_pretend/caracteristicas_totais
        
        return response


def print_menu():
    print("\t\t\t*** MENU PRINCIPAL ***")
    print("\t\t\t===========================")
    print("\t\t\t| 1. Carregar dados.       |")
    print("\t\t\t| 2. Vizualizar dados.     |")
    print("\t\t\t| 3. Descarregar dados.    |")
    print("\t\t\t| 4. Probabilidades.       |")
    print("\t\t\t| 5. Fechar o programa.    |")
    print("\t\t\t===========================")
    print("\t\t\tDigite uma das opcoes acima: ")

def print_menu_probability():
    print("\t\t\t*** MENU PROBABILIDADES ***")
    print("\t\t\t===========================")
    print("\t\t\t| 1. Probabilidade de ocorrencia apriori.                                   |")
    print("\t\t\t| 2. Probabilidade de ocorrencia com intervalo de valores.                  |")
    print("\t\t\t| 3. Probabilidade de ocorrencia condicional.                               |")
    print("\t\t\t| 4. Probabilidade de ocorrencia apriori com intervalo de valores.          |")
    print("\t\t\t| 5. Voltar ao menu principal.                                              |")
    print("\t\t\t===========================")
    print("\t\t\tDigite uma das opcoes acima: ")
    
def chek_path_name(path_to_file):
    try:
        file = open(path_to_file,'r')
        file.close()
        return True
    except:
        return False
def ask_column_name():
    print("\t\t\t===========================")
    response=input("\t\t\t| Por favor informe o nome da coluna que voce gostaria de carregar: ")
    print("\t\t\t===========================")
    return response

def ask_value():
    print("\t\t\t===========================")
    response=input("\t\t\t| Por favor informe do valor do qual voce gostaria de saber a probabilidade de aparecimento: ")
    print("\t\t\t===========================")
    return response
def ask_range(position_range):
    print("\t\t\t===========================")
    response=int(input("\t\t\t| Por favor informe {} do intervalo que voce gostaria de saber a probabilidade de aparecimento: ".format(position_range) ) )
    print("\t\t\t===========================")
    return response
def print_explanation_condicional():
    print("\t\t\t===========================")
    print("\t\t\t| Pora a probabilidade condicional iremos precisar perguntar sobre uma coluna |")
    print("\t\t\t| e um valor extras, para chegarmos se o valor desejado nesse coluna tambem   |")
    print("\t\t\t| possui o valor desejado em outra coluna.  |")
    print("\t\t\t===========================")
def print_explanation_apriori_condicional():
    print("\t\t\t===========================")
    print("\t\t\t| E a uniao da pesquisa condicional com a apriori, aqui nos vamos perguntar   |")
    print("\t\t\t| sobre uma coluna extra e um intervalo de valores nessa coluna. |")
    print("\t\t\t===========================")
def menu_probability(extrator):
    option=0
    while (option != 5):
        print_menu_probability()
        option=int(input())
        if(option==1): 
            print(extrator.probabilidade_apriori(ask_column_name(),ask_value()))          
        elif(option==2):
            print(extrator.probabilidade_intervalo(ask_column_name(),ask_range("inicio"),ask_range("final")))
        elif(option==3):
            print_explanation_condicional()
            print(extrator.probabilidade_condicional(ask_column_name(),ask_value(),ask_column_name(),ask_value()))
        elif(option==4):
            print_explanation_apriori_condicional()
            print(extrator.probabilidade_apriori_intervalo(ask_column_name(),ask_value(),ask_column_name(),ask_range("inicio"),ask_range("final")))
        elif(option==5):
            break
    
def print_view_load_data_read_colum():
    print("\t\t\t===========================")
    print("\t\t\t| Por favor informe o nome das colunas que você gostaria de carregar     |")
    print("\t\t\t| separando-as por espaco. |")
    print("\t\t\t===========================")


def print_view_load_path_name():
    print("\t\t\t===========================")
    print("\t\t\t| Por favor informe o caminho e o nome do arquivo .csv que você gostaria |")
    print("\t\t\t| de carregar os arquivos. |")
    print("\t\t\t===========================")

def print_view_load_data_read_lenght_lines():
    print("\t\t\t===========================")
    print("\t\t\t| Por favor informe a quantidade de linhas que você gostaria de carregar |")
    print("\t\t\t===========================")
    
def print_sucsses():
    print("\t\t\t===========================")
    print("\t\t\t| Operacao realizada com sucesso |")
    print("\t\t\t===========================")

def print_error(erro):
    print("\t\t\t===========================")
    print("\t\t\t| Ocorreu um erro. {} |".format(erro))
    print("\t\t\t===========================")

def main():
    extrator=0
    
    option=0
    
    while (option != 5):
        print_menu()
        option = int(input())
        if(option==1):
            
            print_view_load_path_name()
            path=input()
            
            cheker=chek_path_name(path)
            while(cheker==False):
                print_error("O caminho informado ate o arquivo e invalido, por favor verifique todo o caminho, barras, e nomes das pastas e do arquivo, sua extencao .csv")
                print_view_load_path_name()
                path=input()
                cheker=chek_path_name(path)
                
            print_view_load_data_read_colum()
            list_columns = input().split(" ")
            
            print_view_load_data_read_lenght_lines()
            num_lines=int(input())
            
            extrator= ExtratorDeProbabilidades(path,list_columns)
            extrator.carregar_colunas(list_columns,num_lines)
            print_sucsses() 
                        
        elif(option==2):
            if(extrator!=0):
                if(len(extrator.data_csv)>0):
                    for i in extrator.data_csv:
                        print(i)
                else:
                    print_error("Os dados foram descarregados, por favor carregue novos dados.")
            else:
                print_error("Por favor carregue os dados antes de tentar vizualiza-los")
        elif(option==3):
            if(extrator!=0):
                extrator.descarregar()
                print_sucsses()
            else:
                print_error("Por favor carregue os dados antes de tentar vizualiza-los")
        elif(option==4):
            if(extrator!=0):
                if(len(extrator.data_csv)>0):
                    menu_probability(extrator)
                else:
                    print_error("Os dados foram descarregados, por favor carregue novos dados.")
            else:
                print_error("Por favor carregue os dados antes de tentar vizualiza-los")
        elif(option==5):
            exit(0)
main()