import program_files.check_using_threads as threads_check
import program_files.check_using_processes as proc_check
import program_files.text_generator as generator



def get_text():
    
    while True:
        choice = input("Do you want to specify directory with text files for analysys (enter 'S(pecify)' or 's(pecify)')\n or you prefer to generate text files automatically? (enter 'A(uto)' or 'a(uto)')\nIf you want to exit - enter 'E(xit)' or 'e(xit)':  ")
        match choice.lower().strip():
            case 'a' | 'auto':
                return generator.generate()
            case 's' | 'specify':
                return None
            case 'e' | 'exit':
                print('Program will be finished by user`s choice')
                exit()
            case _:
                pass



def choose_check_type(path):
        while True:
            choice = input("Do you want to use threads (enter 'T(hreads)' or 't(hreads)')   \n or you prefer to use processes& (enter 'P(rocesses)' or 'p(rocesses)')\nIf you want to exit - enter     'E(xit)' or 'e(xit)':  ")
            match choice.lower().strip():
                case 't' | 'threads':
                    return threads_check.check_files(path)
                case 'p' | 'processes':
                    return proc_check.check(path)
                case 'e' | 'exit':
                    print('Program will be finished by user`s choice')
                    exit()
                case _:
                    pass

if __name__ == '__main__':
    path = get_text()
    result = choose_check_type(path)
    print(result)
    with open('./src/results.log', 'w', encoding='UTF-8') as f:
        f.write(str(result))

