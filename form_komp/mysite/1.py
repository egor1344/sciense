from course.models import Course

c = Course.objects.all()
for j in c:
    print(j)