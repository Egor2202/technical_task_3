import typing
import utils


def read_nums_from_file(filename) -> typing.List:
    content = open(filename, 'r').read()
    return list(map(int, content.split(' ')))


def main():
    nums = read_nums_from_file("data/nums.txt")
    print('Минимальное: ', utils.min_num(nums))
    print('Максимальное: ', utils.max_num(nums))
    print('Сумма: ', utils.sum_nums(nums))
    print('Произведение: ', utils.mul_nums(nums))


if __name__ == '__main__':
    main()
