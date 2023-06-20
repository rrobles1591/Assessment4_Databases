"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    description = db.Column(db.String(100), 
                            nullable=False)
    


class Song(db.Model):

    """Song."""
    __tablename__ = "Song"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False,
                     unique=False)
    artist = db.Column(db.String(100), 
                       nullable=False)
    



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_song"

    id = db.Column(db.Integer,
                   autoincrement=True)
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey("Playlist.id"),
                     primary_key=True,)
    song_id = db.Column(db.Integer, 
                        db.ForeignKey("Song.id"),
                        primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
