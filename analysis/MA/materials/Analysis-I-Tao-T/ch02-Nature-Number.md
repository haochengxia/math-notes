# 第二章 从自然数开始

我们在对于在生活中使用代数规则来解决问题已经习以为常，那么为什么代数规则有用？而这可以用数字系统的基本性质来证明。这个过程要求我们思考为什么一个显然的陈述是显然的。这里我们需要重点掌握的是数学归纳法的使用。

```Plaintext
自然数 N => 整数 Z => 有理数 Q => 实数 R
```

数字系统可以按照上方的顺序被构建。

## 2.1 皮亚诺（Peano）公理

皮亚诺公理是一种定义自然数的标准方法。

**不正式**地说自然数是集合`N`中的元素，而`N`由从0开始不断向前数（counting forward）的数字构成。

```Plaintext
幂 => 乘 => 加 => 计数（counting forward or incrementing）
```

定义自然数的两个基本概念：零数字`0`和自增（increment）操作。用类C语法表示自增即为`++`。重新定义`N`。

```Plaintext
N 包含 0,0++,(0++)++,((0++)++)++, ...
```

**公理2.1.** `0`是自然数。

**公理2.2.** 如果`n`是自然数，那么`n++`也是自然数。

**公理2.3.** `0`不是任何自然数后面的那个数字，即后继数（successor）。

**公理2.4.** 不同的自然数一定有不同的后继数。

**公理2.5.** 令`P(n)`是适用于自然数`n`的性质，假设`P(0)`为真且无论何时若`P(n)`为真，`P(n++)`也为真。那么对于任意的自然数n，`P(n)`为真。

> 公理2.1-2.5即为自然数的皮亚诺公理。

这五条公理将是我们对数字做出的唯一假设。在此基础上发展建立所有其他的数字系统，创建函数，做代数和微积分。

*"while each individual natural number is finite, the set of natural numbers is infinite"*，每一个自然数是有限的（根据公理2.5），但是自然数的集合是无限的。

---

*"The great discovery of the late nineteenth century was that numbers can be understood **abstractly** via axioms, without necessarily needing a concrete mode."* 抽象确实是人类智慧的最重要的部分。

---

## 2.2 加法

递归定义自然数加法。

**定义2.2.1.（自然数加法）** 令`m`为自然数。给`m`加上`0`，定义 `0 + m := m`。（归纳地）假设已经定义了如何给`m`加上`n`，把给`m`加上`n++`定义为`(n++) + m := (n + m)++`。

```Plaintext
e.g. 1 + m= (0++) + m = m++
     2 + m= (1++) + m = (m++)++
     ...
```

实际上就是定义了两个式子：`0 + m = m`和`(n++) + m = (n + m)++`。

**引理2.2.2.** 对于任意自然数`n`，`n + 0 = n`。

证明：使用归纳方法，首先`0 + 0 = 0`（因为`0 + m = m`）。假设`n + 0 = n`，判断`(n++) + 0` 是否等于`n++`。根据`(n++) + m := (n + m)++`， `(n++) + 0 = （n+0）++ = n++`。$\square$

**引理2.2.3.** 对于任意自然数`n`和`m`，`n + (m++) = (n + m)++`。

证明：首先固定`m`，并考虑`n = 0`，此时 `0 + (m++) = (0 + m)++`，根据加法的定义，上式成立。接下来继续使用归纳法，假设`n + (m++) = (n + m)++`，然后判断`(n++) + (m++)`是否等于`((n++) + m)++`。根据定义左边部分`(n++) + (m++) = (n + (m++))++`，又根据假设变为`((n + m)++)++`，而右边部分可以直接根据定义变为`((n + m)++)++`，因此等式成立。$\square$

证明`n++ = n + 1`：固定`m`为`0`，那么根据引理2.2.3，可以得到`n + (0++) = (n + 0)++`，又根据引理2.2.2，`n + 0 = n`，所以`n + 1 = n++`。$\square$

根据已有的定义和引理，可以导出加法的**交换（commutative）律、结合（associative）律和消去律（cancellation law）**。

交换律：

- 对于任意的自然数`n`和`m`，`n + m = m + n`；

- 证明：固定`m`，如果`n = 0`，根据定义和引理2.2.2 `m + 0 = 0 + m`。继续使用归纳方法，假设`n + m = m + n`，证明`(n++) + m=m + (n++)`即可。$\square$

结合律：

- 对于任意的自然数`a`，`b`，`c`，`(a + b) + c = a + (b + c)`

- 证明：固定b和c，考虑`a=0`，假设`(a + b) + c = a + (b + c)`，需证`((a++) + b) + c = (a++) + (b + c)`$\square$

消去律：

- `a`，`b`，`c`是满足`a + b = a + c`的自然数，那么`b = c`。

- 证明：考虑`a = 0`的情况，此时`0 + b = 0 + c`根据定义和引理2.2.2，`b = c`，随后用归纳方法，假设`a`具有性质若`a + b = a + c`则`b = c`，需证`(a++) + b = (a++) + c`则`b = c`，根据加法定义`(a++) + b = (a + b)++`， 而`(a++) + c = (a + c)++`，根据公理2.4，`a + b = a + c`，又根据假设条件，`b = c`。$\square$

**定义2.2.7.（正自然数）** 当且仅当一个自然数n不等于0，n被称为正自然数。

**引理 2.2.10.**  令a为一个正自然数，那么一定有且仅有一个自然数b满足b++=a。

证明：首先考虑a为1的基本情况，此时存在自然数b满足b++=a，b=0。然后证明0具有唯一性。如果存在b’++=a，根据公理2.4，b’=b=0，因此b具有唯一性。现在假设有正自然数a同时有且仅有一个自然数b满足b++=a，需要证明对于正自然数a++有唯一的自然数b++满足(b++)++=a++。根据公理2.4，由b++=a可以得出(b++)++=a++，而b++的唯一性同样可以由公理2.4得出。$\square$

**定义2.2.11.（自然数的排序）** 令n和m为自然数。我们称n大于等于m并记作$n \ge m$或$m \le n$当且仅当存在自然数a使得n=m+a成立。而我们称n严格大于m，记作$n > m$或$m < n$当且仅当$n \ge m$同时$n \neq m$。

> 没有最大的自然数n，因为一定有下一个数n++。

**命题 2.2.12.** 自然数排序的基本性质包括：

1. 自反性：$a \ge a$；
2. 传递性：若$a \ge b$且$b \ge c$，那么$a \ge c$；
3. 反对称性：若$a \ge b$且$b \ge a$，那么$a = b$；
4. 加法保留排序：$a \ge b$当且仅当$a+c \ge b+c$；
5. $a < b$当且仅当$a$++ $\le b$；
6. $a < b$当且仅当存在正自然数d使得$b = a + d$；

**命题 2.2.13.（自然数的三分法）** 令a和b是自然数，有且仅有一条陈述是为真：$a < b$，$a = b$，或$a > b$。

证明（*与书上有所不同*）：首先证明一定至多有一条陈述是为真。首先证明$a < b$和$a > b$不会同时成立。

假设 $a < b \land a > b$，有
$$a = b + c, c\neq 0$$

$$b = a + d, d\neq 0$$

将下面的式子代入上面的式子，有
$$a = a + (d + c) 且 c,d \neq 0$$

此时根据命题2.2.6 $d + c = 0$，再根据推论2.2.9，可知$d = c = 0$，产生矛盾。

因此$a < b$和$a > b$不会同时成立。

根据定义，如果$a = b$成立时，$a < b$和$a > b$均不成立。

综上，一定至多有一条陈述为真。

接下来证明至少有一条陈述为真。

令b固定，在a上进行归纳。当a为0时，对于所有的自然数b，$a \leq b$，也就是$a < b$或$a = b$必有一条成立。现在假设a满足该命题，需要证明a++也满足。

根据命题2.2.12，若$a > b$或$a = b$，$a++ > b$。
若$a < b$，$a++ \le b$，$a++ < b$或$a++ = b$必有一条成立。$\square$

**命题 2.2.14 （强归纳法原理）** 令$m_0$为自然数，使得P(m)为任意一个自然数m的性质。假设对于每一个$m \ge m_0$，我们有下面的隐含关系：如果P(m’)对所有的自然数$m_0 \le m’ < m$为真，那么P(m)也为真。随后我们可以推断对于任意的自然数$m(m \ge m_0)$，P(m)为真。

证明：令n为一个自然数，并令Q(n)为对于任意的自然数$m(n > m \ge m_0)$，P(m)为真这一性质。随后在n上进行归纳，n为0时由于不存在有意义的m，Q(n)为真。随后假设Q(n)为真，根据题设，可得P(m)为真, $n \ge m \ge m_0$，因此Q(n++)为真。$\square$

## 2.3 乘法

**定义2.3.1.（自然数的乘法）** 令m为一个自然数，m乘以0（把0乘到m上），我们定义其为$0 \times m := 0$。现在归纳地假设我们已经定义了如何把n乘到m上。然后我们可以把n++乘到m上通过定义$(n++) \times m:= (n \times m) + m$。

**引理2.3.2.（交换律）** 令n，m为自然数，$n \times m = m \times n$。

证明：仍旧使用归纳法，固定m，当n为0时，根据定义$n \times m = 0$，而$m \times n = m \times 0 = 0$可以通过归纳法和定义证明。随后需要证明，若n时成立，n++时也成立。

$$(n++) \times m = (n \times m) + m  = (m \times n) + m = m \times (n++)$$

证毕。$\square$

**引理2.3.3.（正自然数没有零因子）** 令n，m为自然数，$n \times m = 0$当且仅当n和m中至少有一个为0。如果n和m都是正的没那么nm也是正的。

证明：令n，m，a，b，c，d均为自然数，n=a++，m=b++，即n和m均为正自然数。
此时$nm = (a++)(b++)  = a(b++) + (b++) = ab + a + (b++) \iff nm = c + d, d \neq 0$，因此nm为正自然数。$\lnot (n$为正自然数$\land m$为正自然数)，即n和m中至少有一个非正自然数，即n和m中至少一个为0。$\square$

**命题2.3.4.（分配律）** 对于任意的自然数a，b，c，我们$a(b + c) = ab + ac$和$(b + c)a = ba + ca$。

证明：由乘法交换律，只需要证明第一个式子$a(b + c) = ab + ac$。我们保持a和b固定，在c上进行归纳。当c=0时，$a(b + 0) = ab + a0$，化简后$ab = ad$，此时成立。然后假设$a(b + c) = ab + ac$，证明$a(b + (c++)) = ab + a(c++)$。左侧$a(b + (c++)) = (b + c)a + a = ab + ac + a$。右侧$ab + a(c++) = ab + ac + a$。等式成立。$\square$

**命题2.3.5.（结合律）** 对于任意的自然数a，b，c，有$(a \times b) \times c = a \times (b \times c)$。

证明：同样固定a和b固定，在c上进行归纳。c=0时，根据引理2.3.3，左右两侧均为0，等式成立。假设对c，有$(a \times b) \times c = a \times (b \times c)$，需证$(a \times b) \times (c++) = a \times (b \times (c++))$。左侧$(a \times b) \times (c++) = (a \times b) \times c + (a \times b)$。右侧$a \times (b \times (c++)) = a \times (b \times c + b) = a \times (b \times c) + (a \times b) = (a \times b) \times c + (a \times b)$。等式成立。 $\square$

**命题2.3.6.（乘法保留顺序）** 如果a，b是自然数满足$a < b$，并且c为正自然数，那么$ac < bc$。

证明：因为$a < b$，存在正自然数d使得$b = a + d$。乘以并使用分配律得到$bc = ac + dc$。因为d和c都是正自然数，因此dc时正自然数，因此$ac < bc$。 $\square$

**推论2.3.7.（消去律）** 令a，b，c为自然数使得ac = bc且c不为0，那么a=b。

证明：根据命题2.2.13，a和b的关系存在三种情况：$a < b$，$a = b$或$a > b$。假设$a < b$，那么根据命题2.3.6，$ac < bc$，得出矛盾。$a > b$的情况类似。$\square$

**命题2.3.9.（欧几里得算法）** 令n为自然数，q为正自然数。那么存在自然数m和r使得$0 \le r < q$且$n = mq + r$。

证明：固定q在n上进行归纳，对于n=0的情况，令m和r为0，$n = 0q + 0$成立。假设对于一个自然数n有$n = mq + r, (0 \le r < q)$，需证$n++ = m’q + r’, (0 \le r’ < q)$。

根据假设$n++ = (mq + r)++ = mq + (r++)$。

又因为$0 \le r < q$，因此$r++ \le q$，下面分情况讨论：

- $r++ < q$，满足条件；
- $r++ = q$，$$n++ = mq + q = (m++) \times q = (m++) \times q + r’, r’=0$$

证毕。$\square$

**定义2.3.11（自然数的指数运算）** 令m是一个自然数，为了引入m的0次方，定义$m^0 := 1$。特别地，我们定义$0^0 := 1$。现在递归地假设$m^n$已经被定义，定义$m^{n++} := m^n \times m$。