# Import the Evernote client
from evernote.api.client import EvernoteClient

# Import the Evernote note storetypes to get note datatypes 
# to properly get note/tag counts (note filter)
import evernote.edam.notestore.ttypes as NoteStoreTypes

# Define access token either:
# Developer Tokens (https://dev.evernote.com/doc/articles/dev_tokens.php)
# or OAuth (https://dev.evernote.com/doc/articles/authentication.php)
access_token = "insert dev or oauth token here"

# Setup the client
client = EvernoteClient(token = access_token, sandbox = True)

# Get note store object
note_store = client.get_note_store()

# Create note filter object
note_filter = NoteStoreTypes.NoteFilter()

# Set note filter search grammer to get notes created in the last 2 days
note_filter.words = "created:day-2"

# Uncommend the following line to set note filter tag GUIDs
#note_filter.tagGuids = ["GUID of tag1", "GUID of tag 2", "...."]

# Set note filter order to descending
note_filter.ascending =  False

# Set note filter inative attribute to False (will search only active notes)
# setting this value to True will only return search results that are in the trash
note_filter.inactive = False

# Uncomment the following line to set note time zone of the search to 'America/Los_Angeles'
#note_filter.timeZone = "America/Los_Angeles"

# Uncomment the following line to set note filter emphasized attribute to additional 
# 'wish list' search grammer to be used in conjunction with the orinigal search query to 
# highlight search results 
#note_filter.emphasized = "any: tag:cool -tag:uncool"

# Uncomment the following line to set note filter includeAllReadableNotebooks attribute
# to include all readable business notebooks in a search
# search must be performed on a business note store with a business auth token
#note_filter.includeAllReadableNotebooks=True

# (Boolean) Include note/tags that are in the trash in your note counts
include_trash = True

# Returns an object which maps the number of notes captured by the filter to the corresponding
# notebook GUID
note_counts = note_store.findNoteCounts( note_filter, include_trash )

if note_counts.notebookCounts != None:
	print "Found results from %s notebooks" % len(note_counts.notebookCounts)
	for notebook in note_counts.notebookCounts:
		print "     Notebook with GUID %s has %s note(s) that match the filter" % (notebook, note_counts.notebookCounts[notebook])
if note_counts.tagCounts != None:
	print "Found results from %s tags" % len(note_counts.notebookCounts)
	for tag in note_counts.tagCounts:
		print "     Tag with GUID %s has %s note(s) that match the filter" % (tag, note_counts.tagCounts[tag])
if not note_counts.tagCounts and not note_counts.notebookCounts:
	print "No results"