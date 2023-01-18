N = int(input())
alpha_dict = dict()
for i in range(N):
  word = list(input())
  word_length = len(word)
  
  for j in range(word_length):
    if word[j] not in alpha_dict:
      alpha_dict[word[j]] = 10 ** (word_length - j - 1)
    else:
      alpha_dict[word[j]] += 10 ** (word_length - j - 1)

result = list(alpha_dict.values())
result.sort(reverse=True)
now = 9
answer = 0
for i in range(len(result)):
  answer += result[i] * now
  now -= 1
print(answer) 