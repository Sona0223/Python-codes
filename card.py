import sys

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        X = int(data[index + 1])
        index += 2
        
        even_count = N // 2
        odd_count = N - even_count
        
        if X % 2 == 0:
            # X is even, choose even numbers excluding X
            choices = even_count - 1
        else:
            # X is odd, choose odd numbers excluding X
            choices = odd_count - 1
        
        results.append(str(choices))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
