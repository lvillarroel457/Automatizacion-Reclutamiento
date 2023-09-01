
class ContactInformation:
    def __init__(self, emails=None, phones=None, addresses=None, linkedins=None, websites=None):
        self.emails = emails if emails else []
        self.phones = phones if phones else []
        self.addresses = addresses if addresses else []
        self.linkedins = linkedins if linkedins else []
        self.websites = websites if websites else []

    def to_json(self):
        return {
            "emails": self.emails,
            "phones": self.phones,
            "addresses": self.addresses,
            "linkedins": self.linkedins,
            "websites": self.websites
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(
            emails=json_data.get('emails'),
            phones=json_data.get('phones'),
            addresses=json_data.get('addresses'),
            linkedins=json_data.get('linkedins'),
            websites=json_data.get('websites')
        )

    def __str__(self):
        return (
            f"Emails: {', '.join(self.emails) if self.emails else 'N/A'}\n"
            f"Phones: {', '.join(self.phones) if self.phones else 'N/A'}\n"
            f"Addresses: {', '.join(self.addresses) if self.addresses else 'N/A'}\n"
            f"LinkedIn Profiles: {', '.join(self.linkedins) if self.linkedins else 'N/A'}\n"
            f"Websites: {', '.join(self.websites) if self.websites else 'N/A'}"
        )
