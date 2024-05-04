// На основе решения А. Богданова
const B = 4;
begin
  var data := Readlines('27-10b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var pairs := data.Skip(1).Take(n); 
  var sum := pairs.Sum(x->x.Max);
  pairs.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Max)    // из каждой группы выбрать максимальное
               .ToArray)
    .Where(x->not x.Divs(B))
    .Max
    .Print;      
end.


