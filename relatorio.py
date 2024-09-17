from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

pdf.add_page()

pdf.titulo("Análise da Desigualdade na Educação Brasileira")
pdf.sub_titulo("Acesso Desigual e Desafios Regionais no Ensino Superior Brasileiro")
pdf.imagem("imagem.jpg", 10, 90, 180)
pdf.ln(160)
pdf.linha_centralizada("Autora: Lucila Melo - 2024")
pdf.linha_centralizada("Data: 9 de Setembro de 2024")


pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo(" Através dos dados analisados que foram retirados do site https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil (MEC). A desigualdade educacional no Brasil tem uma forte correlação com a distribuição regional de instituições de ensino superior.A distribuição de cursos de graduação por estado no Brasil segue um padrão influenciado por fatores socioeconômicos e demográficos. Os estados mais populosos e desenvolvidos, como São Paulo e Minas Gerais, concentram o maior número de instituições e cursos superiores. Essas regiões possuem uma infraestrutura educacional mais robusta, com mais universidades públicas e privadas oferecendo uma ampla variedade de cursos..")


pdf.imagem("Grafico_Distribuição-De_Cursos.png", 30, 95, 130)
pdf.ln(120)

pdf.paragrafo("Como podemos ver no Gráfico acima, São Paulo (SP) É o estado com a maior oferta de cursos de graduação, abrigando muitas das principais universidades públicas, como USP e UNICAMP, além de um grande número de instituições privadas.")


pdf.add_page()
pdf.imagem("Numero_Cursos_Administrativa_SP.png", 30, 30, 130)
pdf.ln(140)

pdf.paragrafo("Minas Gerais (MG):O segundo estado com maior oferta de cursos, possuindo universidades federais de destaque, como a UFMG e a UFJF, além de uma vasta rede de faculdades privadas.")

pdf.imagem("Numero_Cursos_Administrativa_MG.png", 30, 180, 130)
pdf.ln(120)



pdf.add_page()

pdf.titulo_base("Distribuição dos Cursos EAD e Presenciais.")

pdf.paragrafo("A distribuição de cursos por modalidade no Brasil é marcada principalmente pela oferta em dois formatos: presencial e a distância (EaD). Com o avanço das tecnologias e as necessidades regionais e econômicas, a modalidade EaD tem crescido rapidamente, especialmente nos últimos anos.")

pdf.imagem("Grafico_Distribuição_Cursos_Modalidade.png", 40, 70, 130)
pdf.ln(93)

pdf.paragrafo("Os cursos presenciais seguem o modelo tradicional, onde os alunos frequentam aulas em uma instituição física. A maior parte dos cursos presenciais ainda se concentra nas grandes regiões metropolitanas e em estados como São Paulo,  e Minas Gerais, onde há uma maior concentração de universidades e faculdades. A modalidade presencial é mais predominante em instituições públicas, especialmente nas universidades federais e estaduais, onde a qualidade de ensino é um grande atrativo. No entanto, o acesso a esses cursos é limitado pela quantidade de vagas e pela alta competitividade nos vestibulares.")

pdf.paragrafo("A modalidade EaD vem crescendo substancialmente, especialmente em instituições privadas. A flexibilização do ensino e a possibilidade de atingir regiões mais distantes, onde a infraestrutura educacional é escassa, fazem do EaD uma opção viável para muitos estudantes. Apesar de ampliar o acesso, o EaD enfrenta desafios relacionados à qualidade de ensino e ao suporte oferecido aos estudantes, que muitas vezes precisam de disciplina e autogestão para acompanhar os conteúdos.")



pdf.add_page()
pdf.titulo_base("Os cursos mais procurados")

pdf.paragrafo("Os 10 cursos de graduação mais comuns no Brasil refletem áreas de grande demanda no mercado de trabalho, bem como uma ampla oferta pelas instituições de ensino, especialmente nas modalidades presencial e a distância (EaD). Esses cursos abrangem tanto áreas de ciências humanas e sociais quanto de exatas e saúde.")

pdf.imagem("Grafico_Cursos_Comuns.png", 10, 70, 180)
pdf.ln(120)

pdf.paragrafo("Esses cursos são populares por atenderem à alta demanda de mercado em áreas fundamentais como educação, saúde, gestão, e engenharia. Muitos deles, como Administração, Pedagogia e Ciências Contábeis, também se beneficiam da expansão do ensino a distância, o que facilita o acesso de estudantes em todo o Brasil.")



pdf.add_page()
pdf.titulo_base("Cursos mais procurado em cada Estado")

pdf.paragrafo("Os cursos mais procurados em cada estado do Brasil variam de acordo com as características socioeconômicas, culturais e demandas do mercado de trabalho local. Abaixo estão  o gráfio e algumas informações sobre os cursos mais populares em diferentes estados e as razões por trás de sua alta procura:")

pdf.imagem("Grafico_Cursos_Procurados_Estado.png", 10, 70, 180)
pdf.ln(130)

pdf.paragrafo(" São Paulo é o principal centro econômico e industrial do Brasil. A alta procura por cursos de Administração e Engenharia reflete a necessidade de profissionais capacitados para atender às grandes empresas, indústrias e setores financeiros. Medicina é popular devido à forte infraestrutura de saúde e hospitais de referência na capital paulista, como o Hospital das Clínicas.")


pdf.paragrafo("A demanda por Pedagogia e Administração está relacionada à necessidade de formação de professores e gestores para o setor público e privado, respectivamente. O curso de Medicina é popular devido à carência de médicos na região Nordeste, especialmente em áreas rurais.")



pdf.add_page()
pdf.titulo_base("Número de curso por categoria Administrativa")

pdf.paragrafo("A distribuição de cursos de graduação no Brasil entre instituições públicas e privadas apresenta uma grande diferença em termos de quantidade e oferta. As instituições privadas dominam o cenário educacional brasileiro em número de cursos oferecidos, enquanto as públicas têm menor número, mas com alta procura e prestígio.")

pdf.imagem("Grafico_Numero_Cursos_Categoria_Administrativa.png", 40, 70, 130)
pdf.ln(110)

pdf.paragrafo("Aproximadamente 25% a 30% dos cursos de graduação no Brasil são oferecidos por instituições públicas. Embora o número de instituições públicas seja menor, elas geralmente concentram mais estudantes em cursos de longa duração e com alta demanda, como Medicina, Direito, Engenharia e Licenciaturas. A maioria dos cursos oferecidos por instituições públicas é na modalidade presencial, devido à estrutura mais tradicional dessas universidades.")

pdf.paragrafo("Cerca de 70% a 75% dos cursos de graduação são oferecidos por instituições privadas. Esse número é substancialmente maior devido ao grande número de faculdades e universidades particulares espalhadas pelo país. As instituições privadas lideram a oferta de cursos a distância (EaD), que se expandiu rapidamente nos últimos anos. Muitos cursos como Administração, Pedagogia e Ciências Contábeis são oferecidos na modalidade EaD para atender à alta demanda de alunos que não podem frequentar aulas presenciais.")



pdf.add_page()
pdf.titulo_base(" Vagas autorizadas por Região")


pdf.paragrafo("A distribuição de vagas autorizadas no ensino superior no Brasil varia amplamente entre as regiões, refletindo fatores como densidade populacional, desenvolvimento econômico e infraestrutura educacional. Aqui está uma análise por região:")

pdf.imagem("Grafico_Vagas_Por_Regiao.png", 40, 60, 130)
pdf.ln(110)

pdf.paragrafo("Sudeste: A região Sudeste concentra o maior número de vagas autorizadas para cursos de graduação no Brasil, especialmente em estados como São Paulo, Minas Gerais e Rio de Janeiro. ")

pdf.paragrafo("Nordeste:O Nordeste possui uma quantidade expressiva de vagas, com destaque para estados como Bahia, Pernambuco e Ceará. ")

pdf.paragrafo("Sul: A região Sul, incluindo os estados do Rio Grande do Sul, Santa Catarina e Paraná, também apresenta uma grande oferta de vagas, principalmente em universidades públicas como a UFPR, UFRGS e UFSC, além de diversas instituições privadas. ")

pdf.paragrafo("Norte: A região Norte tem a menor oferta de vagas autorizadas em comparação com outras regiões, com destaque para o estado do Pará. ")

pdf.paragrafo("Centro-Oeste: O Centro-Oeste, que inclui Goiás, Mato Grosso, Mato Grosso do Sul e o Distrito Federal, tem uma oferta de vagas significativa, principalmente em instituições federais como a UnB.")

pdf.paragrafo("Essa distribuição reflete as desigualdades regionais do Brasil, onde as regiões mais ricas e desenvolvidas oferecem mais oportunidades de ensino superior, enquanto o Norte e o Nordeste dependem cada vez mais de alternativas como o EaD para ampliar o acesso à educação.")
pdf.ln(20)

pdf.titulo_base(" Conclusão")

pdf.paragrafo("A desigualdade educacional no Brasil é uma manifestação direta das disparidades regionais, econômicas e sociais que afetam o país. Enquanto regiões mais desenvolvidas e ricas oferecem mais oportunidades de ensino, com maior variedade de cursos e infraestrutura, regiões menos favorecidas enfrentam barreiras para ampliar o acesso à educação superior. Programas de inclusão, como o FIES e o ProUni, e o crescimento do EaD têm ajudado a mitigar parte dessas desigualdades, mas há uma necessidade urgente de políticas públicas que ampliem o acesso à educação de qualidade em todas as regiões do Brasil.")

pdf.output("AnaliseMEC.pdf")