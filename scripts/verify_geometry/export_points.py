origin = None
points = set()
for sketch in App.getDocument('layout').findObjects():
    for geometry in sketch.Geometry:
        if geometry.TypeId == 'Part::GeomPoint':
            points.add((geometry.X, geometry.Y))
        elif geometry.TypeId == 'Part::GeomLineSegment':
            points.add((geometry.StartPoint[0], geometry.StartPoint[1]))
            points.add((geometry.EndPoint[0], geometry.EndPoint[1]))
        elif geometry.TypeId == 'Part::GeomCircle':
            point = (geometry.Center[0], geometry.Center[1])
            if geometry.Radius > 1.9:
                origin = point
            else:
                points.add(point)
        elif geometry.TypeId == 'Part::GeomArcOfCircle':
            points.add((geometry.StartPoint[0], geometry.StartPoint[1]))
            points.add((geometry.EndPoint[0], geometry.EndPoint[1]))
            points.add((geometry.Center[0], geometry.Center[1]))
        else:
            print(geometry.TypeId)

contents = '{} {}\n\n{}\n'.format(origin[0], -origin[1], '\n'.join('{} {}'.format(point[0], -point[1]) for point in points))
with open('geometry.txt', 'w') as file:
    file.write(contents)
