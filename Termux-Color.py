print('\033[1;32m__________________________________________________________\033[1;30m\033[1;32m_\033[1;30m______________\033[1;31mT_E_R_M_U_X\033[1;30m______\033[1;31mC_O_L_O_R_S\033[1;30m _____________\033[1;32m_\033[1;30m\033[1;32m_\033[1;30m___\033[1;30m________________\033[1;31mBY:__Keven_Pratico\033[1;30m___________________\033[1;32m_\033[1;32m_\033[1;30m_______________________\033[1;31mPOR: KEIPI\033[1;30m_______\033[1;30m________________\033[1;32m_\033[1;32m_\033[1;30m________________________\033[1;30m_\033[1;31mLENDA\033[1;30m__________________________\033[1;32m_\033[1;30m\033[1;32m_\033[1;30m_________________________\033[1;31mCOLOR\033[1;30m____________________\033[1;30m______\033[1;32m_\033[1;30m\033[1;32m_\033[1;30m_________________________\033[1;31mCOLOR\033[1;30m__________________________\033[1;32m_\033[1;32m__________________________________________________________')
name = input('\033[1;37mqual é o teu nome?\n')
print('bem-vindo ao termux-color,%s!' % name)


db = {}
print('\033[1;34m__________________________________________________________')
while True:
    print('\033[1;34m__________________________________________________________')
    print(' \033[1;37m qual cor voçe quer ao teu termux?')
    print('\033[1;31m1:Vermelho\033[1;32m   2:Verde \033[1;33m 3:Amarelo\033[1;35m  4:Rosa   \033[1;30m5:Preto  \033[1;34m6:Azul  \033[1;37m 7:Branco \033[1;36m 8:Azul descaregado\033[1;37m ou exit para sair')
    action = input()
    if action == '1':
            k = input('toca enter: ')
            print(' \033[1;31mVermelho')
            
    elif action == '2':
        k = input('tocar enter: ')
        if not k in db:
            print(' \033[1;32mVerde')
            
    elif action == '3':
        k = input('toca enter:')
        print(' \033[1;33mAmarelo')
        
    elif action == '4':
       k = input('toca enter:')
       print(' \033[1;35mRosa')
       
    elif action == '5':
    	k = input('tocar enter:')
    	print(' \033[1;30mPreto')
    elif action == '6':
        k = input('tocar enter:')
        print('\033[1;34mAzul')
    elif action == '7':
    	k = input('tocar enter:')
    	print(' \033[1;37mBranco')
    	
    elif action == '8':
    	k = input('tocar enter:')
    	print(' \033[1;36mAzul ')
    	
    elif action == 'exit':
        print('\033[1;31mA sair ...')
        break
