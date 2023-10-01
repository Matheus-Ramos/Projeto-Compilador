#Gramatica

simbolosTerminais = ['loop', 1, 2, 3, 4, 5, '15_min', '20_min', '1_hora', '1_dia', '2_dias', 'sem limite', 'navegador', ';']
simbolosNTerminais = ['programa_SOL', 'vezes', 'sequência', 'Present', 'tempo', 
                      'fases_EPIC', 'Explore', 'Interact', 'Critique', 'navegar',
                      'visualizar_pdf', 'visualizar_vídeo', 'videoconferência',
                      'whatsapp_web', 'email', 'browser', 'link_pdf', 'link_video',
                      'link_videoconferencia', 'link_whatsapp_web', 'link_email']

#Regras
'''
programa_SOL => loop vezes sequência
sequência => Present tempo 
            | fases_EPIC
fases_EPIC => Explore Present Interact Critique
Explore => navegar tempo ; 
           | Explore
Present => visualizar_pdf 
           | visualizar_vídeo 
           | videoconferência tempo;
Interact => whatsapp_web 
            | email 
            | videoconferência tempo;
Critique => whatsapp_web 
            | email 
            | videoconferência tempo;
vezes => | 1 
         | 2 
         | 3 
         | 4 
         | 5
tempo => | 20_min 
         | 1_hora 
         | 1_dia 
         | 2_dias 
         | sem limite
         | 15_min
navegar => browser
visualizar_pdf => browser link_pdf
visualizar_vídeo =>  browser link_video
videoconferência =>  browser link_videoconferencia
whatsapp_web =>  browser link_whatsapp_web
email =>  browser link_email
browser =>  navegador       #executar o Chrome no computador#
'''