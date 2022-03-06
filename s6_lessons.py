import re # module regexp

with open('dir/s6_lessons.txt', 'r', encoding='utf-8') as f:

    d = {
            x: sum(map(int, filter(lambda x: x.isdigit(), re.split('\D+', y))))
            for x, y in (line.split(':')
            for line in f.readlines())
        }

    print(d)
