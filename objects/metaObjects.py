class Contact:
    def __init__(self, _phone = None, _fax = None, _email = None, _website = None, _mobile = None):
        self.phone = _phone
        self.fax = _fax
        self.email = _email
        self.website = _website
        self.mobile = _mobile
        #Social
        self.facebook = None
        self.vk = None
        self.instagram = None
        self.twitter = None
        self.youtube = None
        self.ok = None
        self.webcam = None
        self.telegram = None
        self.whatsapp = None
        self.linkedin = None
        self.pinterest = None
        self.viper = None
        self.foursquare = None
        self.skype = None
        self.xing = None
        self.vhf = None
        self.flickr = None
        self.mastodon = None
        self.sip = None
        self.diaspora = None
        self.gnusocial = None
        # TODO support custom social tags MAYBE: there should ne no need


class Address:
    def __init__(self, _housenumber = None, _street = None, _place = None,
     _city = None, _postcode = None, _country = None, _suburb = None, _state = None, _province = None):
        self.housenumber = _housenumber
        self.street = _street
        self.place = _place
        self.city = _city
        self.postcode = _postcode
        self.country = _country
        self.suburb = _suburb
        self.state = _state
        self.province = _province