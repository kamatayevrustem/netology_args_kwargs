# Разработать свою реализацию функции print - adv_print.
# Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:
# 1) start - с чего начинается вывод. По умолчанию пустая строка;
# 2) max_line - максимальная длина строки при выводе. Если строка превыщает max_line,
# то вывод автоматически переносится на новую строку;
# 3) in_file - аргумент, определяющий будет ли записан вывод ещё и в файл.

import math


def adv_print(text, start='', max_line=None, in_file=False):

    if in_file:
        f = open('out.txt', 'w')

    print(start)

    if in_file:
        f.write(start)
        f.write('\n')

    if max_line is None or len(text) <= max_line:
        print(text)

        if in_file:
            f.write(text)
    else:
        lines_for_print = math.ceil(len(text) / max_line)
        text_residue = text
        for i in range(lines_for_print):
            text_for_print = text_residue[0: max_line]
            print(text_for_print)
            if in_file:
                f.write(text_for_print)
                f.write('\n')
            text_residue = text_residue[max_line:]

    if in_file:
        f.close()


def main():
    text = '123456789012345678901234567890123456789'
    adv_print(text, max_line=10, in_file=True)


if __name__ == '__main__':
    main()
