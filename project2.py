import random


def generate(n):
    seq = ''
    tmpl = 'ACGT'
    random.seed()
    for i in range(n):
        v = random.randint(0, 3)
        seq += tmpl[v]
    return seq


def countA(seq):
    n = 0
    if len(seq) < 1E6:
        for i in range(len(seq)):
            if seq[i] == 'A':
                n = n+1
    else:
        partdone = len(seq) // 10
        for i in range(len(seq)):
            if seq[i] == 'A':
                n = n+1
            if i % partdone == 0:
                print(f'\t progress.. %{(i // partdone * 10)}')

    return n


def countC(seq):
    n = 0
    if len(seq) < 1E6:
        for i in range(len(seq)):
            if seq[i] == 'C':
                n = n + 1
    else:
        partdone = len(seq) // 10
        for i in range(len(seq)):
            if seq[i] == 'C':
                n = n + 1
            if i % partdone == 0:
                print(f'\t progress.. %{(i // partdone * 10)}')

    return n

def countG(seq):
    n = 0
    if len(seq) < 1E6:
        for i in range(len(seq)):
            if seq[i] == 'G':
                n = n + 1
    else:
        partdone = len(seq) // 10
        for i in range(len(seq)):
            if seq[i] == 'G':
                n = n + 1
            if i % partdone == 0:
                print(f'\t progress.. %{(i // partdone * 10)}')

    return n

def countT(seq):
    n = 0
    if len(seq) < 1E6:
        for i in range(len(seq)):
            if seq[i] == 'T':
                n = n + 1
    else:
        partdone = len(seq) // 10
        for i in range(len(seq)):
            if seq[i] == 'T':
                n = n + 1
            if i % partdone == 0:
                print(f'\t progress.. %{(i // partdone * 10)}')

    return n

def percentA(seq):
    return 100.0 * countA(seq)/len(seq)


def percentC(seq):
    return 100.0 * countC(seq) / len(seq)


def percentG(seq):
    return 100.0 * countG(seq) / len(seq)


def percentT(seq):
    return 100.0 * countT(seq) / len(seq)


def find_key(key, seq):
    found_list = []
    for i in range(len(seq)):
        if seq[i] == key:
            place = str(seq[i].index(seq[i]))
            found_list += place
    return found_list


def main():
    while 1:
        s = input('Press q to quit or a positive integer: ')
        if s == 'q':
            print('Program exits.')
            break
        n = int(s)
        seq = generate(n)

        # find counts and percentages of sequence
        pcntA = percentA(seq)
        pcntG = percentG(seq)
        pcntC = percentC(seq)
        pcntT = percentT(seq)

        a_count = countA(seq)
        g_count = countG(seq)
        c_count = countC(seq)
        t_count = countT(seq)

        # print results
        print(f"'A' count is : {a_count}")
        print('The sequence is %.2f%% A.' % pcntA)
        print(f"'C' count is: {g_count}")
        print('The sequence is %.2f%% G.' % pcntG)
        print(f"'C' count is {c_count}")
        print('The sequence is %.2f%% C.' % pcntC)
        print(f"'T' count is: {t_count}")
        print('The sequence is %.2f%% T.' % pcntT)

        # search for subsequence
        key = input("Enter a subsequence to search for: ").upper()
        found = find_key(key, seq)
        print(f"{key} found at following positions: {found}")
        print('----------------------------')


main()