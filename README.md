# Google Scholar Python to Check New Entries

This project was created in the spring of 2020 for the Northwestern University Chemical Engineering newsletter, in order to obtain newly published articles every week from a list of professors. This would allow the department to add these new articles to the newsletter without pestering professors weekly.


## Prerequisite

```bash
pip install scholarly
```
## Notes

All professors are included in professor list except for:
- P. Daniels
- G. Holderfield
- B. Johnson
- M. Kulkarni
- S. Lichter
- M. Werwath

whose articles in Google Scholar do not link to their pages. This list can be modified as professors join or leave the department.

After running the script in google_scholar_panorama.py, new results since the last check is in new_add_result, which can then be added to the newsletter.

## License

[MIT](https://choosealicense.com/licenses/mit/)
