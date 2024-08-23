from enum import unique
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from app import db

# Models go here:


class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    image = db.Column(db.String, nullable=False)

    @validates("name", "image")
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f"{key} field must be completed.")
        else:
            return value


class Album(db.Model, SerializerMixin):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    year = db.Column(db.Integer, nullable=False)
    song = db.Column(db.String, nullable=False)
    artist_name = db.Column(db.String, nullable=False)

    @validates("name", "song", "year")
    def validate_name_year_song(self, key, value):
        if not value:
            raise ValueError(f"{key} field must be completed.")
        else:
            return value


class AlbumReview(db.Model, SerializerMixin):
    __tablename__ = "albumreviews"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.String)

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"))

    @validates("rating")
    def validate_rating(self, key, value):
        if not (isinstance(value, int)) and (0 <= value <= 10):
            raise ValueError(f"{key} must be a number between 0 and 10.")
        else:
            return value

    @validates("artist_id", "album_id")
    def validates_albums_artists(self, key, value):
        if not (isinstance(value, int)):
            raise ValueError(f"{key} must be an Integer.")
        else:
            return value
