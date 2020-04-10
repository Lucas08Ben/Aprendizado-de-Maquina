# Aprendizado de Máquina

Fevereiro de 2019

### Lista 1 - Visão Geral
### Universidade Federal do Ceará - Campus de Quixadá
### Professor Regis Pires Magalhães

# O que é Aprendizado de Máquina e para que serve?
Aprendizado de Máquina é a ciência de programar computadores a aprenderem a partir de dados. O Aprendizado de máquina facilita o trabalho dos desenvolvedores de forma com o que eles não precisem criar um algoritmo altamente específico para determinada tarefa, tornando mais viável a criação dele, pois o Aprendizado de Máquina melhora sua performance a partir de uma experiência que ele obtém.

# O que são dados rotulados (labels) e para que servem?
São dados que determinam o que as features significam. Um conjunto de features determinam uma label. As labels são utilizadas para que o algoritmo consiga definir um modelo que se encaixe no problema e para que utilize as informações dadas para realizar a solução. 

# Quais os problemas mais comuns de aprendizado supervisionado?

Problemas de Regressão e problemas de classificação

# Quais os problemas mais comuns de aprendizado não-supervisionado?
Clusterização

# Que tipo de algoritmo de Machine Learning (ML) você usaria para:
## Permitir um robô andar em diversos tipos de terreno?
Seria utilizado aprendizado supervisionado de classificação, para ele classificar o terreno e utilizar o seu determinado recurso para operar sobre o terreno.
## Segmentar clientes em múltiplos grupos?
Seria utilizado aprendizado não-supervisionado, para ele detectar padrões e determinar em quais grupos cada cliente deve se encaixar.

# O que é um sistema de aprendizado online? Quais suas vantagens e desvantagens?
Em aprendizado Online o sistema é treinado incrementalmente, sendo alimentado por instâncias sequenciais.

* Vantagens:
	1. O sistema aprende novos dados à medida que eles chegam.
	2. Cada um desses novos aprendizados são rápidos e baratos.
	3. Quando os dados são aprendidos, não são mais necessários,
portanto podem ser excluídos para que não possa gerar um
montante de dados.
	4. Pode usar o aprendizado out-of-core
* Desvantagens:
	1. Se dados ruins forem disponibilizados ao sistema, a performance do sistema irá cair gradualmente

# O que significa aprendizado out-of-core?
Out-of-core é quando um sistema tenta aprender a partir de um conjunto de dados maior que sua memória, então o algoritmo aprende esses dados por partes até que ele tenha sido completa mente aprendido.

# Que tipo de aprendizado usa medidas de similaridade para fazer predições?
É utilizado o instance-based learning. O sistema aprende os exemplos e então gera para novos casos usando a medida de similaridade.

# Em um modelo de ML, qual a diferença entre parâmetros e hiper-parâmetros?
A diferença é que um hiper-parâmetro não é afetado pelo próprio algoritmo de aprendizado e deve ser definido antes do treinamento e permanecer constante.

# O que são e qual a diferença entre Underfitting e Overfitting? O que fazer para solucionar cada um desses problemas?

• Overfitting acontece quando o modelo é muito complexo em relação ao quantidade e distorção dos dados de treinamento. Uma forma de reduzir o Overfitting é simplificando o modelo, usando um com menos parâmetros, ter mais dados de treino e até mesmo reduzindo a distorção nos dados de treino.
• Underfitting é o contrário do Overfitting, ou seja, acontece quando o seu modelo é muito simples para aprender a estrutura dos dados. Uma forma de concertar isso é escolhendo um modelo mais poderoso, com mais parâmetros, é possível também disponibilizando melhores características para o algoritmo de aprendizagem e reduzindo as restrições no modelo.

# Para que servem: conjunto de treino, conjunto de validação e conjunto de teste?
Estes conjuntos servem para obter o resultado de como o modelo está performando. O conjunto de treino é a base de dados utilizada para treinar o modelo, já o conjunto de teste serve para testar de forma definitiva o modelo  que apresentou melhor resultados a partir dos resultados obtidos com o conjunto de dados de validação.

# O que significa validação cruzada e qual a vantagem de usá-la ao invés de usar um conjunto de validação?
Validação Cruzada significa utilizar o conjunto de testes, separá-la em subconjuntos complementares e cada modelo é treinado com uma combinação diferente desses subconjuntos e validado com as restantes partes. A maior vantagem é que não há desperdício de dados para realização de validação. A desvantagem é que o processamento pode ser muito mais pesado do que um processo de aprendizagem normal. 
