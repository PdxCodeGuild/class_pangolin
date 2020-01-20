def update_all_clans():    
    # ------------------ get all clan data:-----------------------
    added_to_db_counter = 0         # number added to db
    counter = 0                     # total number for WG API
    for realm_url in ['com', 'ru', 'eu', 'asia']:
        # add clans to DB.  API returns list of up to 100 ("count") of clans at a time
        page_num = 1                    # page num sent to API.  currently about 145 pages of clans in NA
        count = 100                     # count of clans per page.  usually 100, but drops to 0 once all clans have been listed
        while count != 0:
            payload = {
                'application_id': api_key,
                'page_no': page_num,
            }
            response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/clans/list/", params=payload)
            page_query = json.loads(response.text)

            for clan in page_query['data']:
                counter += 1
                if realm_url == 'com':
                    realm = 'NA'
                elif realm_url == 'ru':
                    realm = 'RU'
                elif realm_url == 'eu':
                    realm = 'EU'
                elif realm_url == 'asia':
                    realm = 'SEA'

                # get clan and then update info
                c, was_created = Clan.objects.get_or_create(clan_wgid = clan['clan_id'], clan_realm=realm)
                c.clan_tag = clan['tag']
                c.clan_name = clan['name']
                c.clan_members_count = clan['members_count']
                c.save()

                if was_created:
                    added_to_db_counter += 1

            # print status message to console every 500 clans
            if counter % 500 == 0:
                print(f"Retrieved {counter} of {page_query['meta']['total']} clans from {realm} server.")

            # update loop vars        
            page_num += 1
            count = page_query['meta']['count']

        # completed realm message
        print(f"Completed retrieving {page_query['meta']['total']} clans from {realm} server.")

    # verify clan load was successful
    print(f'{counter} clans across all realms, from WG API. {added_to_db_counter} new DB additions')
