#Напишите программу, которая запрашивает у пользователя последовательно день его рождения, месяц и год

var a,b,c:integer;

begin
  writeln('В каком году ты родился?');
  readln(a);
  writeln('Какой сейчас год?');
  readln(b);
  c:=b-a;
  if (c mod 10 = 0) or (c mod 10 > 4)
  then writeln('Тебе в этом году ',c,' лет')
  else if (c mod 10 = 1)
         then writeln('Тебе в этом году ',c,' год')
         else writeln('Тебе в этом году ',c,' года')
end.
