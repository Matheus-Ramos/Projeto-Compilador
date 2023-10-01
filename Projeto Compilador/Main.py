import AnalizadorLexico as alx
import AnalizadorSintatico as ast

simbolosTerminais = ['loop', 1, 2, 3, 4, 5, '15_min', '20_min', '1_hora', '1_dia', '2_dias', 'sem limite', 'navegador', ';']
simbolosNTerminais = ['programa_SOL', 'vezes', 'sequência', 'Present', 'tempo', 
                      'fases_EPIC', 'Explore', 'Interact', 'Critique', 'navegar',
                      'visualizar_pdf', 'visualizar_vídeo', 'videoconferência',
                      'whatsapp_web', 'email', 'browser', 'link_pdf', 'link_video',
                      'link_videoconferencia', 'link_whatsapp_web', 'link_email']

lex = alx.A_Lexico()
tokens = lex.lexico()

parser = ast.A_Sintatico(tokens)
parser.parse() # Inicia a análise sintática.