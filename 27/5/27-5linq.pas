// На основе решения А. Богданова
uses sf;
const B = 5;
begin
  var data := Readlines('27-5b.txt').Sel(s->s.ToIs).ToA;
  var n := data[0].First;
  var pairs := data.Skip(1).Take(n); 
  var sum := pairs.Sum(x->x.Min);
  pairs.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Min)    // из каждой группы выбрать минимальное
               .ToA)
    .Where(x->x.Divs(B))
    .Print;      
end.


