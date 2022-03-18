## 분할 정복

```
function F(x):
	if F(x)가 간단 then:
		return F(x)를 계산한 값 - (정복)
	
	else:
		x 를 부분문제 x1, x2로 분할
		F(x1) 과 F(x2) 를 호출
		return F(x1), F(x2)로 F(x)를 구한 값 - (조합, 분할)
```

