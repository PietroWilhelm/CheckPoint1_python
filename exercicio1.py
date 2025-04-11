nome = input('nome: ')
salario_fixo = float(input('salario fixo: '))
tv_seg_qua = float(input('quantas vendas foram feitas: '))
tv_qui_sex = float(input('quantas vendas foram feitas: '))
tv_sab_dom = float(input('quantas vendas foram feitas: '))

comissao_seg_qua = tv_seg_qua * 0.2 #20/100
comissao_qui_sex = tv_qui_sex * 0.15 #15/100
comissao_sab_dom = tv_sab_dom * 0.1 #10/100

total_comissao = comissao_seg_qua + comissao_qui_sex + comissao_sab_dom
valor_total = salario_fixo + total_comissao

print(valor_total)