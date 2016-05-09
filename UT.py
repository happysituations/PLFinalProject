class teacher(object):

    def f(self):
        data = {
            'name': 'Staff',
            '$name': lambda x: data.update({'name': x}),

            'course': 'n/a',
            '$course': lambda x: data.update({'course':x}),

            'military time': 0000,
            '$military time': lambda x: data.update({'military time': x}),

            'professor rating': 0,
            '$professor rating': lambda x: data.update({'professor rating':x}),

            'statement': "",
            '$statement': lambda x: data.update({'statement':x})
        }

        def cf(self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf

    run = f(1)


'''
print a.run('course name')
a.run('$course name')('cs')
print a.run('course name')
print

print a.run('course number')
a.run('$course number')('329e')
print a.run('course number')
print

print a.run('military time')
a.run('$military time')('1700')
print a.run('military time')
print

print a.run('professor rating')
a.run('$professor rating')(3.4)
print a.run('professor rating')

'''