# Implementação de uma Fila de Processos

Este repositório contém a implementação de uma **fila de processos** utilizando listas encadeadas em Python. Este código foi desenvolvido como parte do desafio do curso de **Ciência de Dados na Ampli**, abordando os conceitos de **pilhas e filas**.

## 📌 Descrição
O programa implementa uma estrutura de dados do tipo **fila** utilizando **listas encadeadas**. A fila segue a estrutura **FIFO** (*First In, First Out*), onde os elementos são inseridos no final e removidos do início.

## 🚀 Como Usar
### 🔧 Execução
1. Certifique-se de ter o **Python 3** instalado.
2. Salve o código em um arquivo `fila.py`.
3. Execute o arquivo com o comando:
   ```bash
   python fila.py
   ```

### 🔄 Funcionamento
O programa cria uma fila, adiciona alguns elementos e os remove, exibindo o estado da fila antes e depois da remoção.

## 📜 Explicação do Código

### **Classe Item**
```python
class Item:
    def __init__(self, valor=None, proximo=None):
        self.valor = valor
        self.proximo = proximo
```
A classe `Item` representa um elemento da fila, contendo:
- `valor`: O valor armazenado no item.
- `proximo`: Referência ao próximo item da fila.

### **Classe Fila**
```python
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
```
A classe `Fila` implementa uma **fila dinâmica** utilizando **listas encadeadas**. 
- `self.primeiro`: Aponta para o primeiro item da fila.
- `self.ultimo`: Aponta para o último item da fila.

#### **Método `push(valor)`**
```python
    def push(self, valor):
        item = Item(valor)
        if self.primeiro:
            self.ultimo.proximo = item
            self.ultimo = item
        else:
            self.primeiro = item
            self.ultimo = item
```
Este método **adiciona um elemento ao final da fila**.
- Se a fila estiver vazia, o elemento se torna o **primeiro e último**.
- Caso contrário, o novo elemento é anexado ao final.

#### **Método `pop()`**
```python
    def pop(self):
        self.primeiro = self.primeiro.proximo
```
Este método **remove o primeiro elemento** da fila.

### **Função `main()`**
```python
    def main():
        fila = Fila()
        fila.push(1)
        fila.push(2)
        fila.push(3)
        print(fila)
        fila.pop()
        print(fila)
```
A função `main()`:
1. Cria uma fila.
2. Adiciona três elementos (1, 2, 3).
3. Exibe o estado da fila.
4. Remove o primeiro elemento e exibe novamente a fila.

### **Execução do Programa**
```python
if __name__ == '__main__':
    main()
```
O programa inicia chamando `main()` quando executado.

## 📚 Conclusão
Este código apresenta uma **solução temporária via software** para a implementação de uma **fila de processos** utilizando listas encadeadas. Ele pode ser expandido para incluir outras operações, como exibição detalhada da fila, tamanho da fila, ou implementação de uma fila circular.

---
🔹 *Desenvolvido como parte do curso de Ciência de Dados na Ampli.*

## 📞 Contato
- GitHub: [Isaque Almeida](https://github.com/IsaqueAlmeida)
- LinkedIn: [Isaque F. S. Almeida](https://www.linkedin.com/in/isaque-f-s-almeida/)
