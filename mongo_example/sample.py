from models import sample


if __name__ == '__main__':
    sample.TestUser.objects.create(first_name='1', last_name='2')

    breakpoint()
    print("end")
