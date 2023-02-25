def query_by_id(user_id):
    print('123')

def query_by_name(user_name):
    print('234')

def main():
    while True:
        option = input('345')
        if option == '1':
            user_id = input('243434')
            query_by_id(user_id)
        elif option == '2':
            user_name = input('24242424')
            query_by_name(user_name)
        elif option == 'exit':
            print('退出！')
            break
        else:
            print('输入无效，请重新输入')


if __name__ == '__main__':
    main()
