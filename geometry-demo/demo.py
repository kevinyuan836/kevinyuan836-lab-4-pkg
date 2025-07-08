from geometry import shapes, utils


a = shapes.Square(3)
b = shapes.Circle(4)
c = shapes.Square(2)

print(f"Area of the first square {a.area()}")
print(f"Area of the first circle {b.area()}")
print(f"Area of the second square {c.area()}")

stats = utils.area_stats(a,b,c)
print(stats)