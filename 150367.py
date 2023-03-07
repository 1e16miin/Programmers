def is_btree(binary_number):
    
    N = len(binary_number)
    
    if N == 1: #리프 노드는 0, 1 상관없음
        return True
    
    if "1" not in binary_number: #원소가 전부 0인 서브 트리
        return True
    
    mid = N // 2
    if binary_number[mid] == "0":
        return False
    
    return is_btree(binary_number[:mid]) and is_btree(binary_number[mid+1:])

def solution(numbers):
    answer = []
    for number in numbers:
        binary_number = bin(number)[2:]
        saturation = bin(len(binary_number) + 1)[2:]
        if "1" in saturation[1:]:
            padding = int('0b' + len(saturation) * '1',2) - len(binary_number)
            binary_number = "0" * padding + binary_number
        result = is_btree(binary_number)
        answer.append(1 if result else 0)
        
    return answer
