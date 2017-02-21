class Property:
    '''
    Is showing details of properties.
    '''
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Printing information about property.
        Returning None
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        '''
        Returning dictionary of main property characteristic which where printed.
        '''
        return dict(square_feet=input("Enter the square feet: "),
         beds=input("Enter number of bedrooms: "),
         baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    '''
    Is creating valid input arguments and returning input.
    '''
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    '''
    This class is updating information about property.
    '''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Is showing details of property
        Returning None
        '''
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? " "({})".format(", ".join(Apartment.valid_balconies)))
            parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    def prompt_init():
        '''
        Is updating dictionary with new information and returning it.
        '''
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    '''
    Is getting information about house.
    '''
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
        garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        This function is printing information about house.
        Returning None
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        '''
        Is updating dictionary with new information about house and returning it.
        '''
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
        House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
        House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage, "num_stories": num_stories})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''
    Is giving information about house for purchase.
    '''
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Printing information about house for purchase.
        Returning None
        '''
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        '''
        Updating dictionary with new information about purchasing and returning it.
        '''
        return dict(
        price=input("What is the selling price? "),
        taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    '''
    Is giving information about house for rental.
    '''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Is printing information about house for rental.
        Returning None
        '''
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        '''
        Is updating dictionary with new information about house for rental and returning it.
        '''
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    '''
    Is giving information about house.
    '''
    def prompt_init():
        '''
        Is combining basic information about house with information about house for rental.
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    '''

    '''
    def prompt_init():
        '''
        Is combining basic information about apartment with information about apartment for rental.
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    '''

    '''
    def prompt_init():
        '''
        Is combining basic information about apartment with information about apartment for purchasing.
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    '''

    '''
    def prompt_init():
        '''
        Is combining basic information about apartment with information about house for purchasing.
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    '''
    Is printing whole giving information about house or apartment.
    '''
    type_map = {("house", "rental"): HouseRental, ("house", "purchase"): HousePurchase, ("apartment", "rental"): ApartmentRental, ("apartment", "purchase"): ApartmentPurchase}

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        '''
        Is printing whole information about houses or apartments which are in list of properties.
        Returning None
        '''
        for property in self.property_list:
            property.display()

    def display_work(self, pay, time):
        print('Agent will get {}'.format(pay))
        print('Agent will find house in {}'.format(time))

    def add_property(self):
        '''
        Is adding property with written information iin property list.
         Returning None
        '''
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

purchase = Purchase.prompt_init()
class Agency(Agent):

    valid_agencies = ('low', 'medium', 'high')
    asking = get_valid_input('Choose agency', valid_agencies)

    def agency_poslygu(self):
        if self.asking == 'low':
            agent_payment = int(purchase['price']) / 100 * 5
            search_time = '3 weeks'
        if self.asking == 'medium':
            agent_payment = int(purchase['price']) / 100 * 7
            search_time = '2 weeks'
        if self.asking == 'high':
            agent_payment = int(purchase['price']) / 100 * 10
            search_time = '1 week'
        return agent_payment, search_time

    def prompt_init():
        '''
        Is updating dictionary with new information about house and returning it.
        '''
        parent_init = Property.prompt_init()
        parent_init.update({'Agent payment': Agency().agency_poslygu()[0], 'Customer will be find in': Agency().agency_poslygu()[1]})
        return parent_init

    prompt_init = staticmethod(prompt_init)

class Get_info_about_property:
    def get_info(self):
        agent = Agent()
        agent.add_property()
        agent.display_work(Agency().agency_poslygu()[0], Agency().agency_poslygu()[1])
        agent.display_properties()


