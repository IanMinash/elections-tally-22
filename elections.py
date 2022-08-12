import requests


def get_county_from_code(code: str):
    counties = {
        "049": "prisons",
        "048": "diaspora",
        "047": "nairobi",
        "046": "nyamira",
        "045": "kisii",
        "044": "migori",
        "043": "homa bay",
        "042": "kisumu",
        "041": "siaya",
        "040": "busia",
        "039": "bungoma",
        "038": "vihiga",
        "037": "kakamega",
        "036": "bomet",
        "035": "kericho",
        "034": "kajiado",
        "033": "narok",
        "032": "nakuru",
        "031": "laikipia",
        "030": "baringo",
        "029": "nandi",
        "028": "elgeyo/marakwet",
        "027": "uasin gishu",
        "026": "trans nzoia",
        "025": "samburu",
        "024": "west pokot",
        "023": "turkana",
        "022": "kiambu",
        "021": "murang'a",
        "020": "kirinyaga",
        "019": "nyeri",
        "018": "nyandarua",
        "017": "makueni",
        "016": "machakos",
        "015": "kitui",
        "014": "embu",
        "013": "tharaka - nithi",
        "012": "meru",
        "011": "isiolo",
        "010": "marsabit",
        "009": "mandera",
        "008": "wajir",
        "007": "garissa",
        "006": "taita taveta",
        "005": "lamu",
        "004": "tana river",
        "003": "kilifi",
        "002": "kwale",
        "001": "mombasa",
    }
    return counties[code]


"""
Citizen Digital 

[
    {
        "id":1661,
        "county_id":49,
        "county_name":"PRISONS",
        "county_code":"049",
        "office":"President",
        "registered_voters":7449,
        "voter_turnout":44.44,
        "votes_cast":3311,
        "valid_votes":3291,
        "disputed_votes":0,
        "rejected_ballots":20,
        "rejected_objected_to":0,
        "updated_at":"2022-08-11T07:45:13.000000Z",
        "candidate_votes":[
            {
                "id":418995,
                "candidate_name":"RAILA  ODINGA",
                "candidate_popular_name":"RAILA",
                "candidate_avatar":"https:\/\/elections-portal.s3.eu-west-1.amazonaws.com\/candidates\/VEKJoega8PzWNJ2ZU4X9bknJgT6gvlAWjItbUhHw.webp",
                "office":"President",
                "party":"AZIMIO",
                "party_abbreviation":"AZIMIO",
                "party_color":"#122883",
                "total_votes":2027,
                "percentage":61.22
            },
            {
                "id":418996,
                "candidate_name":"WILLIAM SAMOEI RUTO",
                "candidate_popular_name":"RUTO",
                "candidate_avatar":"https:\/\/elections-portal.s3.eu-west-1.amazonaws.com\/candidates\/e9bMouujN1uZ6GJsUTPMj3AU3GvMab4qezh62Ugi.webp",
                ...
            },
            ...
        ],
    },
    ...
]

"""


def get_tally_from_citizen():
    resp = requests.get(
        "https://elections.citizen.digital/api/county-results?election=4&office=1&with[]=candidateVotes.electionCandidate.party",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.5",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "api-key": "WruVVZTlaI6sAmK0hBGy3xJSeXuXc8yYFh3sVtGGi8VbpgdP+3G8UHWhBAN7pS5mLD650AArASrPGZ+o",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Referer": "https://elections.citizen.digital/",
        },
    )
    tally = []
    resp_json = resp.json()
    for county in resp_json:
        for votes in county.get("candidate_votes", []):
            tally.append(
                {
                    "name": "raila"
                    if votes["candidate_popular_name"] == "RAILA"
                    else "ruto"
                    if votes["candidate_popular_name"] == "RUTO"
                    else "waihiga"
                    if votes["candidate_popular_name"] == "MWAURE"
                    else votes["candidate_popular_name"].lower(),
                    "county": "nairobi"
                    if county["county_name"].lower() == "nairobi city"
                    else "elgeyo/marakwet"
                    if county["county_name"].lower() == "elgeyo marakwet"
                    else county["county_name"].lower(),
                    "votes": int(votes["total_votes"]),
                    "src": "citizen",
                }
            )

    return tally


"""
Nation Media

{
    "national":{
        "candidates":[
            {
                "PRESIDENT_ID":1,
                "FIRST_NAME":"RAILA",
                "LAST_NAME":"ODINGA",
                "SMALL_IMAGE":"odinga.jpg",
                "PARTY_INITIALS":"AZIMIO",
                "COALITION_NAME":"0.00",
                "CANDIDATE_VOTES":6176348,
                "NATIONAL_PERCENTAGE":50.378379365995755
            },
            ...
        ],
        "total_votes_cast":12259918,
        "total_constituencies_reporting":0
    },
    "county":{
        "candidates":[
            {
                "PRESIDENT_ID":1,
                "FIRST_NAME":"RAILA",
                "LAST_NAME":"ODINGA",
                "SMALL_IMAGE":"odinga.jpg",
                "PARTY_INITIALS":"AZIMIO",
                "COUNTY_NO":"047",
                "CANDIDATE_VOTES":690088,
                "TOTAL_PRESIDENT_COUNTY_VOTES_CAST":1182177,
                "COLOURCODES":"031470",
                "COUNTY_PERCENTAGE":58.37433819131991,
                "WINNING":true
            },
            {
                "PRESIDENT_ID":2,
                "FIRST_NAME":"WILLIAM",
                "LAST_NAME":"RUTO",
                "SMALL_IMAGE":"ruto.jpg",
                "PARTY_INITIALS":"UDA",
                "COUNTY_NO":"022",
                "CANDIDATE_VOTES":548087,
                "TOTAL_PRESIDENT_COUNTY_VOTES_CAST":742582,
                "COLOURCODES":"F5C700",
                "COUNTY_PERCENTAGE":73.80827975900304,
                "WINNING":true
            },
            {
                "PRESIDENT_ID":2,
                "FIRST_NAME":"WILLIAM",
                "LAST_NAME":"RUTO",
                "SMALL_IMAGE":"ruto.jpg",
                "PARTY_INITIALS":"UDA",
                "COUNTY_NO":"007",
                "CANDIDATE_VOTES":26658,
                "TOTAL_PRESIDENT_COUNTY_VOTES_CAST":107008,
                "COLOURCODES":"F5C700",
                "COUNTY_PERCENTAGE":24.91215610047847,
                "WINNING":false
            },
            ...
        ]
    },
    "constituencies":{
        "candidates":[
            {},
            ...
        ]
    }
}
"""


def get_tally_from_nation():
    resp = requests.get(
        "https://static.nation.africa/2022/president.json",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "Referer": "https://elections.nation.africa/",
        },
    )
    tally = []
    resp_json = resp.json()
    for votes in resp_json["county"]["candidates"]:
        tally.append(
            {
                "name": "raila"
                if "RAILA" in votes["FIRST_NAME"]
                else "ruto"
                if "RUTO" in votes["FIRST_NAME"]
                else votes["LAST_NAME"].lower(),
                "county": get_county_from_code(votes["COUNTY_NO"].lower()),
                "votes": int(votes["CANDIDATE_VOTES"]),
                "src": "nation",
            }
        )

    return tally


"""
Standard Media

[
    {
        "id":1,
        "county":"MOMBASA",
        "polygon":"county_1.geojson",
        "county_abv":"MBS",
        "votes":[
            {
                "candidate":"Odinga Raila",
                "votes":"156945",
                "avg_percentage_votes":"58.3",
                "party":"AZIMIO",
                "color":"#151FA4"
            },
            {
                "candidate":"Ruto William Samoei",
                "votes":"110323",
                "avg_percentage_votes":"40.7",
                "party":"UDA",
                "color":"#f8c80e"
            }
        ],
        "winner":{
            "candidate":"Odinga Raila",
            "votes":"156945",
            "avg_percentage_votes":"58.3",
            "party":"AZIMIO",
            "color":"#151FA4"
        }
    },
    ...
]
"""


def get_tally_from_standard():

    resp = requests.get(
        "https://www.standardmedia.co.ke/2022elections/counties_results?election=5",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Requested-With": "XMLHttpRequest",
            "Alt-Used": "www.standardmedia.co.ke",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "Referer": "https://www.standardmedia.co.ke/2022elections/",
        },
    )
    tally = []
    resp_json = resp.json()
    for county in resp_json:
        for votes in county.get("votes", []):
            tally.append(
                {
                    "name": "raila"
                    if "Raila" in votes["candidate"]
                    else "ruto"
                    if "Ruto" in votes["candidate"]
                    else votes["candidate"].split(" ")[0].lower(),
                    "county": county["county"].lower(),
                    "votes": int(votes["votes"]),
                    "src": "standard",
                }
            )

    return tally
